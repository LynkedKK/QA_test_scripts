#!/usr/bin/env bash

set -ex

./scripts/clear_report_directory.sh
rm -rf .pytest_cache

mkdir -p reports/functional/test_viewport/food
mkdir -p reports/functional/test_viewport/manage
mkdir -p reports/UI_test/functional/test_happyflow_1/result

rm -rf /home/logic/_del/LYNKED_QA_project-local-chrome/tests/UI_test/functional/smoke_test_remote_parallel/actual/*.png

pipenv sync

pipenv run pytest \
  --workers 10 \
  --maxfail=999 \
  --json-report  \
  --html=reports/functional/index.html \
  -x tests/UI_test/functional/smoke_test_remote_parallel


# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/smoke_test/test_TID_004.py &

# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/smoke_test/test_TID_005.py &

# wait