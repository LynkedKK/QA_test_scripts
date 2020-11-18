#!/usr/bin/env bash

set -ex

function shutdown {
    ./scripts/down_docker_selenium.sh
    echo "Shutdown complete"
}

trap shutdown SIGTERM SIGINT EXIT

# export REPO_HOME=..
# PATH=$PATH:$REPO_HOME/drivers/chrome/85

rm -rf reports/* || true
mkdir -p reports/functional/test_viewport
touch reports/functional/test_viewport/.gitkeep

# sh docs/flows/test_site_flows/build.sh

./scripts/up_docker_selenium.sh

echo 'sleep a while to let docker steady'
sleep 30

pipenv sync

# pipenv run pytest --html=reports/regression/report.html tests/UI_test/regression
pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional
# pipenv run pytest --html=reports/new_feature/report.html tests/UI_test/new_feature
