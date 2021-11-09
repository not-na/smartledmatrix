#!/bin/bash

echo "Killing any remnants of old servers..."
# We can kill the old processes quite hard, since do_refresh.sh should have tried restarting before calling this script
killall -SIGKILL uwsgi

uwsgi server_uwsgi.ini > ./uwsgi.log 2>&1 &
