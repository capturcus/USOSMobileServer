#!/bin/bash
rm uwsgi.log
rm uwsgi
uwsgi --plugin=python --socket usosmobile.sock --module usosmobile.wsgi --chmod-socket=666 --enable-threads > uwsgi.log 2> uwsgi&
