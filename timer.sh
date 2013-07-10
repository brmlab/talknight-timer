#!/bin/bash

DIR="$(dirname $0)"
PYTHON=$DIR/bin/python
TIMER=$DIR/timer.py
$PYTHON $TIMER $*
