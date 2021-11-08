#!/bin/bash

echo "Killing any remnants of old servers..."
killall uwsgi

uwsgi server_uwsgi.ini > uwsgi.log 2>&1 &