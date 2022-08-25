#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static

if [ ! -x /usr/sbin/nginx ]; then
    apt-get -y update
    apt-get -y install nginx
fi

mkdir -p /data/web_static/{releases/test,shared} && echo "<html><head></head><body><h1>hello world</h1></body></html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/:80 default_server;/a location /hbnb_static/ {alias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart
