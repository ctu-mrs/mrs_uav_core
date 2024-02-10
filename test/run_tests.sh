#!/bin/bash

set -e

trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
trap 'echo "$0: \"${last_command}\" command failed with exit code $?"' ERR

# build the packages
catkin build # it has to be fully built normally before building with --catkin-make-args tests
catkin build -DMRS_ENABLE_TESTING=1 --catkin-make-args tests

catkin test -i -p 1 -s
