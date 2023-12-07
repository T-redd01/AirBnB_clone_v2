#!/usr/bin/env bash
# setup server for html stati cpages

sudo apt-get update
sudo apt-get install -y nginx

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Hello World!" > /data/web_static/releases/test/index.html

ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R "ubuntu" /data/
sudo chgrp -R "ubuntu" /data/

sudo cp -a /etc/nginx/sites-available/default{,.copy}
sudo printf "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /data/web_static/current;
	server_name _;

	location /hbnb_static {
		alias /;
		try_files $uri $uri/ =404;
		add_header X-Served-By $HOSTNAME;
	}
}" > /etc/nginx/sites-available/default

nginx -s reload
