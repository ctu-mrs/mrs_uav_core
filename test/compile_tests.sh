#!/bin/bash

set -e

trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
trap 'echo "$0: \"${last_command}\" command failed with exit code $?"' ERR

# build the package
catkin build -DMRS_ENABLE_TESTING=1 # it has to be fully built normally before building with --catkin-make-args tests
catkin build -DMRS_ENABLE_TESTING=1 --catkin-make-args tests
