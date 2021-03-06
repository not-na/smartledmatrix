#!/bin/bash

echo "Refreshing..."

# Get script path, based on https://stackoverflow.com/a/24114056
scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

# Change to root directory
cd $scriptDir/..

# Update dependencies
echo "Updating requirements..."
source venv/bin/activate
pip install -r requirements.txt

if [ -f $UWSGI_PIDFILE ]; then
  echo "uWSGI was running, reloading..."
  ./scripts/reload_server.sh
else
  echo "Server wasn't running, starting it"
  ./scripts/start_server.sh
fi

echo "Done!"