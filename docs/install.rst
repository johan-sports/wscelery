Installation
============

PyPI version (recommended): ::

    $ pip install wscelery

Development version: ::

    $ pip install https://github.com/johan-sports/wscelery/zipball/master


Usage
-----

Launch the websocket listener on port 8001: ::

    $ wscelery --port=8001

Or launch from celery: ::

    $ celery wscelery -A proj --address=127.0.0.1 --port=8001

Broker URL and other configuration options can be passed through standard Celery options: ::

    $ celery wscelery -A proj --broker=amqp://guest:guest@localhost:5672//
