#!/bin/bash

# Get script path, based on https://stackoverflow.com/a/24114056
scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

# Change to build directory
echo "Preparing for build..."
cd $scriptDir/../firmware
mkdir build
cd build

# Perform build
echo "Building..."
cmake ..
make -j4

echo "Uploading..."

# Upload via openocd/swd
# This way we don't need the pico to be in bootsel mode
openocd -f interface/raspberrypi-swd.cfg -f target/rp2040.cfg -c "program firmware.elf
verify reset exit"

echo "Success!"
