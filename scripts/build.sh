#!/usr/bin/env bash

set -ex

# function shutdown {
#     ./scripts/down_docker_selenium.sh
#     echo "Shutdown complete"
# }

# trap shutdown SIGTERM SIGINT EXIT

# # export REPO_HOME=..
# # PATH=$PATH:$REPO_HOME/drivers/chrome/85

# rm -rf reports/* || true
# mkdir -p reports/functional/test_viewport
# touch reports/functional/test_viewport/.gitkeep

# sh docs/flows/test_site_flows/build.sh

# ./scripts/up_docker_selenium.sh

# echo 'sleep a while to let docker steady'
# sleep 30

# pipenv sync

# pipenv run pytest --co -k test
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/smoke_test

rm -rf /home/logic/_del/LYNKED_QA_project-local-chrome/tests/UI_test/functional/smoke_test_remote_parallel/actual/*.png

pipenv sync

pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/smoke_test_remote_parallel/test_TID_004.py
