#!/usr/bin/env bash
printf "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /data/web_static/current;
        server_name _;

        location /hbnb_static {
                alias /;
                try_files $uri $uri/ =404;
                add_header X-Served-By $HOSTNAME;
        }
}" >./file
