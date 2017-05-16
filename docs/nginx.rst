Nginx Usage
===========

The following is a minimal nginx configuration: 

.. code-block:: nginx

  server {
    listen 80;
    server_name wscelery.johan-sports.com;
    charset utf-8;

    location / {
       proxy_pass http://localhost:1337;
       proxy_redirect off;
       proxy_http_version 1.1;
       proxy_set_header Host $host;
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection $connection_upgrade;
    }
  }
