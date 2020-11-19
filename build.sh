#!/usr/bin/env bash

set -ex

# function shutdown {
#     ./scripts/down_docker_selenium.sh
#     echo "Shutdown complete"
# }

# trap shutdown SIGTERM SIGINT EXIT


rm -rf reports/* || true
mkdir -p reports/functional/test_viewport/food
mkdir -p reports/functional/test_viewport/manage
touch reports/functional/test_viewport/food/.gitkeep
touch reports/functional/test_viewport/manage/.gitkeep


# sh docs/flows/test_site_flows/build.sh

# ./scripts/up_docker_selenium.sh
# echo 'sleep a while to let docker steady'
# sleep 30

# pipenv sync

# pipenv run pytest --html=reports/regression/report.html tests/UI_test/regression
pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional
# pipenv run pytest --html=reports/new_feature/report.html tests/UI_test/new_feature
