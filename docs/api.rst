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
    "uuid": "bbef09c9-aff2-4f51-8238-d594fe16bc66",
    "type": "task-sent",
    "name": "myapp.add",
    "retries": 0,
    "eta": 32,
    "routing_key": "default",
    "root_id": 12,
    "parent_id": 15
  }

.. _task-received:

task-received
~~~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "bbef09c9-aff2-4f51-8238-d594fe16bc66",
    "type": "task-received",
    "timestamp": 1494943644.786262,
    "local_received": 1494947444.446089,
    "utcoffset": -2,
    "retries": 1,
    "root_id": 12,
    "parent_id": 15
  }

.. _task-started:

task-started
~~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "bbef09c9-aff2-4f51-8238-d594fe16bc66",
    "type": "task-received",
    "timestamp": 1494943644.786262,
    "local_received": 1494947444.446089,
    "utcoffset": -2
  }

.. _task-succeeded:

task-succeeded
~~~~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "bbef09c9-aff2-4f51-8238-d594fe16bc66",
    "type": "task-succeeded",
    "timestamp": 1494943644.786262,
    "local_received": 1494947444.446089,
    "utcoffset": -2,
    "result": "42",
    "runtime": 5.227228619001835
  }

.. _task-failed:

task-failed
~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "bbef09c9-aff2-4f51-8238-d594fe16bc66",
    "type": "task-failed",
    "timestamp": 1494943644.786262,
    "local_received": 1494947444.446089,
    "utcoffset": -2,
    "traceback": "...",
    "exception": "ValueError('oops')",
  }

.. _task-rejected:

task-rejected
~~~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "bbef09c9-aff2-4f51-8238-d594fe16bc66",
    "type": "task-rejected",
    "requeued": true,
  }

.. _task-revoked:

task-revoked
~~~~~~~~~~~~
.. code-block:: json

  {
    "uuid": "bbef09c9-aff2-4f51-8238-d594fe16bc66",
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
    "uuid": "bbef09c9-aff2-4f51-8238-d594fe16bc66",
    "type": "task-retried",
    "timestamp": 1494943644.786262,
    "local_received": 1494947444.446089,
    "utcoffset": -2,
    "exception": "ValueError('oops')",
    "traceback": "...",
  }
