Examples
========

All following examples are also available in the project `examples directory`_.

.. _`examples directory`:: https://github.com/johan-sports/wscelery/tree/master/examples

Setup
-----

To run these examples we must first create a project with some celery tasks.

.. literalinclude:: ../examples/celery_app/tasks.py
   :language: python
   :caption: tasks.py

This assumes that `RabbitMQ`_ is running in on ``localhost:5672``.

We will also define an endpoint for triggering tasks. In this example we are
using `flask`_, but any other web framework/library will work fine.

To install application dependencies run ``pip install -r examples/celery_app/requirements.txt``
in the project root folder.

.. _RabbitMQ: https://www.rabbitmq.com/
.. _flask: http://flask.pocoo.org/

.. literalinclude:: ../examples/celery_app/app.py
   :language: python
   :caption: app.py

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
given user input and report the finished status. 

First we define a basic HTML file with a form and load jQuery:

.. literalinclude:: ../examples/javascript/index.html
   :language: html
   :caption: index.html

When the form is submitted a request is made to the web API to start the task. We then open
a connection to wscelery and handle different message types reporting the current status. 

.. literalinclude:: ../examples/javascript/client.js
   :language: javascript
   :caption: client.js
