#!/usr/bin/env bash

set -ex

TMP_DIR=$(mktemp -d)
git clone --depth 1 git@github.com:LynkedKK/QA_test_result.git $TMP_DIR

cp -r /home/logic/_workspace/LynkedKK_QA_Offical_repo/reports/functional/ $TMP_DIR

pushd $TMP_DIR
  git add .
  git commit -m"update result,"
  git push
popd