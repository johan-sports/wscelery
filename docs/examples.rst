Examples
========

To run these examples we must first create a project with some celery tasks.
This code can also be found in the `examples directory<https://github.com/johan-sports/wscelery/blob/master/examples/celery_app>`_.

.. code-block:: python

   # tasks.py

   from celery import Celery

   app = Celery('tasks', broker='amqp://guest:guest@localhost:5672')

   @app.task
   def add(x, y):
       return x + y

This assumes that `RabbitMQ`_ is running in on ``localhost:5672``.

We will also define an endpoint for triggering tasks. In this example we are
using `flask`_, but any other web framework/library will work fine.

To install application dependencies run ``pip install -r examples/celery_app/requirements.txt``
in the project root folder.

.. _RabbitMQ: https://www.rabbitmq.com/
.. _flask: http://flask.pocoo.org/

.. code-block:: python

   # app.py

   from flask import Flask

   from tasks import add

   app = Flask(__name__)

   @app.route('/add/<int:x>/<int:y>', method=['POST'])
   def add(x, y):
       task = add.delay(x, y)

   if __name__ == '__main__':
       app.run()


Start the web server with ::

  $ python app.py

To test that the API is working, trigger a task ::
 
  $ curl -X POST http://localhost:5000/add/1/2
  {
    "task_id": "1ee8e9bf-17b9-4fef-90ca-42c0c5880f13"
  }

We must also start a celery worker to process the task ::

  $ celery worker -A tasks

Lastly, run wscelery on localhost and allow all origins: ::

  $ celery wscelery --allow-origin=.*


Javascript
----------

This code is intended to run in the browser. It will trigger the add task for
given user input and report the finished status. The full source can be found
in the `examples directory<https://github.com/johan-sports/wscelery/blob/master/examples/javascript>`_.

First we define a basic HTML file with a form and load jQuery:

.. code-block:: html

  <!-- index.html -->
  <!doctype html>
  <html>
      <head>
          <meta charset="utf-8" />
          <title>WSCelery Client</title>

          <script
              src="https://code.jquery.com/jquery-3.2.1.min.js"
              integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
              crossorigin="anonymous"></script>
          <script src="client.js" type="text/javascript"></script>
      </head>
      <body>
          <form action="" id="add">
              <input name="x" type="number" required />
              <input name="y" type="number" required />
              <input type="submit" value="Add" />
          </form>

          <p id="status"></p>
      </body>
  </html>

When the form is submitted a request is made to the web API to start the task. We then open
a connection to wscelery and handle different message types reporting the current status. 

.. code-block:: javascript

  // client.js
  window.onload = function() {
    function openSocket(taskId) {
      // Connect websocket
      var taskSocket = new WebSocket('ws://localhost:1337/' + taskId);

      taskSocket.onmessage = function(event) {
        var msg = JSON.parse(event.data);

        switch(msg.type) {
        case 'task-succeeded':
          $('p#status').text('Task succeeded with result: ' + msg.result + ' Elapsed: ' + msg.runtime);
          break;
        case 'task-retried': // fallthrough
        case 'task-failed':
          $('p#status').text('Task failed with exception: ' + msg.exception);
          break;
        case 'task-rejected': // fallthrough
        case 'task-revoked':
          break;
        default: // ignore
          break;
        }
      };

      taskSocket.onerror = function(error) {
        $('p#status').text('Websocket error: ' + error.toString());
      };
    }

    $('form#add').submit(function(event) {
      var formData = new FormData(event.target);
      var x = formData.get('x');
      var y = formData.get('y');
      // Create task
      $.ajax({
        url: 'http://localhost:5000/add/' + x + '/' + y,
        type: 'POST',
        success: function(data) {
          $('p#status').text('Received task with ID:', data.task_id);
          openSocket(data.task_id);
        },
        error: function() {
          $('p#status').text('Request to web API failed.');
        }
      });
      event.preventDefault();
    });
  };

Python
------
