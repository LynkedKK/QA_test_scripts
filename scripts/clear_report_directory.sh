#!/usr/bin/env bash

set -ex

rm -rf $(find ./reports |grep -i png)

# rm -rf reports/**/*.png
# rm -rf reports/UI_test/**/*.png