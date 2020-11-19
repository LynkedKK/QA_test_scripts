#!/usr/bin/env bash

set -ex

marp ./helloworld.md &

wait

echo 'done'
