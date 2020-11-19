#!/usr/bin/env bash

set -ex

export PROJ_HOME=/home/logic/_workspace/LYNKED_QA_project
export DOCS_DIR=$PROJ_HOME/docs
export FLOWS_DIR=$DOCS_DIR/flows
export USER_FLOW=$FLOWS_DIR/user_flow
export PATH=$PATH:$USER_FLOW/node_modules/.bin

# mmdc -i happy_flow_1.mmd -o happy_flow_1.png
# mmdc -i happy_flow_1.mmd -o happy_flow_1.png

# npm install

mmdc -i $FLOWS_DIR/restaurant_flow/happyflow-1/happy-flow-1.mmd -o $FLOWS_DIR/restaurant_flow/happyflow-1/happy-flow-1.png &

mmdc -i $FLOWS_DIR/restaurant_flow/happyflow-2/happy-flow-2.mmd -o $FLOWS_DIR/restaurant_flow/happyflow-2/happy-flow-2.png &

wait
