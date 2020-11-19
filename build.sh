#!/usr/bin/env bash

set -ex

# function shutdown {
#     ./scripts/down_docker_selenium.sh
#     echo "Shutdown complete"
# }

# trap shutdown SIGTERM SIGINT EXIT

# ./scripts/clear_report_directory.sh

mkdir -p reports/functional/test_viewport/food
mkdir -p reports/functional/test_viewport/manage
mkdir -p reports/UI_test/functional/test_happyflow_1/result

# touch reports/functional/test_viewport/food/.gitkeep
# touch reports/functional/test_viewport/manage/.gitkeep


# sh docs/flows/test_site_flows/build.sh

# ./scripts/up_docker_selenium.sh
# echo 'sleep a while to let docker steady'
# sleep 30

# pipenv sync

# pipenv run pytest --html=reports/regression/report.html tests/UI_test/regression
pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional
# pipenv run pytest --html=reports/new_feature/report.html tests/UI_test/new_feature

# pipenv run pytest tests/self_test

# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_happyflow_1/test_happyflow_1_chrome.py

# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_happyflow_1/test_happyflow_1_firefox.py
# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_happyflow_1_click_accept_and_continue/test_happyflow_1_chrome_click_acept_and_continue.py

# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_happyflow_1_click_accept_and_continue/test_po_helloworld.py


# pipenv run pytest tests/UI_test/functional/test_viewport/test_SeleniumCoolDown.py
# pipenv run pytest tests/UI_test/functional/test_functional_Helloworld.py

# pipenv run pytest tests/self_test

# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_viewport/test_ViewPort_food.py
# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_viewport/test_ViewPort_manage.py
