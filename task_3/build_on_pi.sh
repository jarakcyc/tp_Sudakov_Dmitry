#!/bin/bash

mkdir tmp
cd tmp

path_to_compillers='/home/dimas/dimas/task_3/tools/arm-bcm2708/arm-rpi-4.9.3-linux-gnueabihf/bin'
export PATH=$PATH:$path_to_compillers

sysroot="./tools/arm-bcm2708/arm-rpi-4.9.3-linux-gnueabihf/arm-linux-gnueabihf/sysroot/"
cmake "~/dimas/task_3/PatternsCollection" -DON_PI=ON -DSYSROOT=$sysroot
make
make install DESTDIR='../installed'
cd ../
zip -r archive.zip installed