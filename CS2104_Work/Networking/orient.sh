#!/bin/sh
 
FIRST_ARGUMENT="$1"
echo "Hello $FIRST_ARGUMENT!"

echo "You were in directory "
pwd
cd ..
echo "which is in directory"
pwd
echo " with "
ls 
