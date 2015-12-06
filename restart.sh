#!/bin/bash
./clean.sh
killall uwsgi
./uwsgi.sh

