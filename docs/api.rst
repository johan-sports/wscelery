=============
API Reference
=============

WSCelery provides a websocket connection under ``ws://my-domain.com/<task-id>``. Once a connection is
established the server sends status updates for the task with ID `<task-id>` to the
client.

It is the client's responsibility to close the connection.

Events
======

The received events mirror those described in the `Celery monitoring reference`_
with some keys excluded.
Events are sent through the websocket as JSON and have the following structure:

.. _`Celery monitoring reference`: http://docs.celeryproject.org/en/latest/userguide/monitoring.html#task-events

.. contents::
    :local:
    :depth: 1

.. _task-sent:

task-sent
~~~~~~~~~
.. code-block:: json

  {
    "uuid": "",
    "type": "task-sent",
    "name": "myapp.add",
    "retries": 0,
    "eta": 32,
    "routing_key": "",
    "root_id": 12,
    "parent_id": 15
  }

.. _task-received:

task-received
~~~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "",
    "type": "task-received",
    "timestamp": ,
    "retries": 1,
    "root_id": 12,
    "parent_id": 15
  }

.. _task-started:

task-started
~~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "",
    "type": "task-received",
    "timestamp": ,
  }

.. _task-succeeded:

task-succeeded
~~~~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "",
    "type": "task-succeeded",
    "timestamp": ,
    "result": "42",
    "runtime": 5.32152
  }

.. _task-failed:

task-failed
~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "",
    "type": "task-failed",
    "timestamp": 
    "traceback": "...",
    "exception": "ValueError('oops')",
  }

.. _task-rejected:

task-rejected
~~~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "",
    "type": "task-rejected",
    "requeued": true,
  }

.. _task-revoked:

task-revoked
~~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "",
    "type": "task-revoked",
    "terminated": true,
    "signum": 3,
    "expired": false
  }

.. _task-retried:

task-retried
~~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "",
    "type": "task-retried",
    "timestamp": ,
    "exception": "ValueError('oops')",
    "traceback": "...",
  }
