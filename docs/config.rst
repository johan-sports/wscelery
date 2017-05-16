:tocdepth: 2

Configuration
=============

WSCelery can be configured from the command line: ::

  $ wscelery --allow-origin=.*

Or using environment variables. All options are configured with a `WSCELERY_` prefix. ::

  $ export WSCELERY_PORT=8001
  $ wscelery  # will use port 8001

Options
-------

Standard celery configuration options can be overriden using environment variables
or command line options. See the `Celery reference`_ for a complete list of celery options.

.. _`Celery reference`: http://docs.celeryproject.org/en/latest/userguide/configuration.html

Celery command line options can be passed to wscelery too. E.g. ::

  $ wscelery --broker=amqp://guest:guest@10.9.3.123:5672

For a full list of celery options see: ::

  $ celery --help

For a full list of wscelery specific options see: ::

  $ wscelery --help

.. contents::
    :local:
    :depth: 1

.. _address:

address
~~~~~~~

Run the websocket server on the given address. (Defaults to `127.0.0.1`)

.. _port:

port
~~~~

Run the websocket server on a given port. (Defaults to `1337`)

.. _allowed_origin:

allowed_origin
~~~~~~~~~~~~~~

A regex of origins allowed to access the websocket. (Defaults to current host)

.. _debug:

debug
~~~~~

Run wscelery in debug mode. **Do not use in production.**
