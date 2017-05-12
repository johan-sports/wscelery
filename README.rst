=========
WS Celery
=========

.. image:: https://img.shields.io/pypi/v/wscelery.svg
    :target: https://pypi.python.org/pypi/wscelery

.. image:: https://travis-ci.org/johan-sports/wscelery.svg?branch=master
    :target: https://travis-ci.org/johan-sports/wscelery

Real time celery monitoring using websockets. Inspired by `flower <https://github.com/mher/flower>`__.

************
Requirements 
************

* Python 3.x

************
Installation
************

PyPI version (recommended): ::

    $ pip install wscelery

Development version: ::

    $ pip install https://github.com/johan-sports/wscelery/zipball/master

*****
Usage
*****

Launch the websocket listener on port 8001: ::

    $ wscelery --port=8001

Or launch from celery: ::

    $ celery wscelery -A proj --address=127.0.0.1 --port=8001

Broker URL and other configuration options can be passed through standard Celery options: ::

    $ celery wscelery -A proj --broker=amqp://guest:guest@localhost:5672//

To see all command options use: ::

    $ wscelery --help

*******
Caveats
*******

* TLS encryption not (yet) supported

*******
License
*******

Licensed under MIT. See the LICENSE file in the project root directory.
