=========
WS Celery
=========

.. image:: https://img.shields.io/pypi/v/wscelery.svg
    :target: https://pypi.python.org/pypi/wscelery

.. image:: https://travis-ci.org/johan-sports/wscelery.svg?branch=master
    :target: https://travis-ci.org/johan-sports/wscelery

.. image:: https://readthedocs.org/projects/wscelery/badge/?version=latest
    :target: http://wscelery.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

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

*************
Documentation
*************

Full documentation can be found on `Read The Docs`_.

.. _`Read The Docs`: https://wscelery.readthedocs.io

*******
Caveats
*******

* TLS encryption not (yet) supported

************
Contributing
************

If you want to contribute, feel free to submit a PR. Please make sure that the tests pass
(run with ``python setup.py test``). Make sure you add your name to `CONTRIBUTORS`_.

.. _`CONTRIBUTORS`: https://github.com/johan-sports/wscelery/tree/master/CONTRIBUTORS

*******
License
*******

Licensed under MIT. See the LICENSE file in the project root directory.
