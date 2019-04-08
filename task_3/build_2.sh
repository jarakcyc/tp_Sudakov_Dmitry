#!/bin/bash

sudo apt-get install libboost-all-dev
sudo apt-get install openssl 
sudo apt-get install libssl-dev
sudo apt-get install libboost-system-dev
sudo apt install curl
sudo apt install libcurl4-openssl-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install gnutls-bin 
sudo apt-get install gsasl
sudo apt-get install libghc-gsasl-dev 
sudo apt install doxygen graphviz
sudo apt-get install libgnutls28-dev 
sudo apt-get install sendmail

mkdir tmp
cd tmp

#export BOOST_ROOT='/home/dimas/dimas/task_3/boost_1_61_0'

cmake "~/dimas/task_3/PatternsCollection/Decorator/cpp-source"
sudo make

cp -r ../PatternsCollection/Decorator/cpp-source/configs .

./Decorator