#!/usr/bin/env bash

set -ex

TMP_DIR=$(mktemp -d)
# git clone --depth 1 git@github.com:LynkedKK/QA_test_result.git $TMP_DIR
git clone --depth 1 https://$GITHUB_TOKEN@github.com/LynkedKK/QA_test_result.git $TMP_DIR

cp -r reports/functional/ $TMP_DIR

cd $TMP_DIR
  git add .
  git commit -m"update result,"
  git push
cd -
