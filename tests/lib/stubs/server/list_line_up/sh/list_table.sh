#!/usr/bin/env bash

set -ex

./t1.sh | tidy > list_table.html

grep -i lid list_table.html > lid_only.raw