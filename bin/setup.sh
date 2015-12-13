#!/bin/bash

apt-get update && apt-get upgrade -y

apt-get install -y nginx python-pip python-dev supervisor

pip install --upgrade -r /vagrant/requirements.txt

ln -s /vagrant/setup/nginx.mud.conf /etc/nginx/conf.d/mud.conf
ln -s /vagrant/setup/supervisor.mud.conf /etc/supervisor/conf.d/mud.conf

rm -rf /etc/nginx/sites-enabled/*
mkdir -p /var/log/mud/

supervisorctl reread
supervisorctl update
supervisorctl start mud

service nginx restart
