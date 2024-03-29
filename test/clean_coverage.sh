#!/bin/bash

set -e

trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
trap 'echo "$0: \"${last_command}\" command failed with exit code $?"' ERR

ORIGINAL_PATH=`pwd`

while [ ! -e ".catkin_tools" ]; do
  cd ..
  if [[ `pwd` == "/" ]]; then
    # we reached the root and didn't find the build/COLCON_IGNORE file - that's a fail!
    echo "$0: could not find the root of the current workspace".
    return 1
  fi
done

cd build

OLD_FILES=$(find . -name "*.gcda")

for FILE in $OLD_FILES; do
  echo "$0: removing old coverage file '$FILE'"
  rm $FILE
done
