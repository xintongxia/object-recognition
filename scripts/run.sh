#!/usr/bin/env bash

if [ -z "$VIRTUAL_ENV" ]; then
  echo "Not running inside virtual env."
  echo "Please setup virtualenv according to README.md."
  exit -1
fi

python main.py "$@"
