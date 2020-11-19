#!/usr/bin/env bash

set -ex

export SCRIPTS_DIR=$(dirname $0)
export REPO_HOME=$(realpath $SCRIPTS_DIR/..)

cd $REPO_HOME/_ref/docker-selenium
  docker-compose -f docker-compose-v3.yml kill
  docker-compose -f docker-compose-v3.yml down
cd $REPO_HOME
