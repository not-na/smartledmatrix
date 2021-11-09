#!/bin/bash

UWSGI_PIDFILE="/tmp/uwsgi.pid"

uwsgi --reload $UWSGI_PIDFILE || ./scripts/start_server.sh