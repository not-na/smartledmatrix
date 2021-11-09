#!/bin/bash

# Usage: ./rsync_push.sh username@host
# Example: ./rsync_push.sh pi@raspberrypi.local
# To prevent password prompts, SSH Key based authentication is recommended

rsync -avz --filter=':- .gitignore' ./ $1:smartledmatrix/
rsync -avz ./config.py $1:smartledmatrix/instance/config.py

ssh $1 ./smartledmatrix/scripts/do_refresh.sh
