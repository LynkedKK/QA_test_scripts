#!/usr/bin/env bash

set -ex

curl -H "Accept: application/vnd.github.everest-preview+json" \
    -H "Authorization: token $GITHUB_TOKEN" \
    --request POST \
    --data '{"event_type": "run-smoke"}' \
    https://api.github.com/repos/LynkedKK/QA_test_scripts/dispatches
