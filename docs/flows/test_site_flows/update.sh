#!/usr/bin/env bash

set -ex

find . |entr -c -s "mmdc -i happy_flow_1.mmd -o happy_flow_1.png"
