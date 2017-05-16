Docker Usage
============

WSCelery is has automatic builds on `DockerHub`_.  

Pull the image and start the container ::

  $ docker pull johansports/wscelery
  $ docker run -p=1337:1337 -d johansports/wscelery

You can also specify environment variables ::

  $ docker run -e"BROKER_URL=amqp://guest:guest@localhost:5672" -e"WSCELERY_ALLOW_ORIGIN=.*" run -d johansports/wscelery

.. _`DockerHub`: https://hub.docker.com/r/johansports/wscelery/
