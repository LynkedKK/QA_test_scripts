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

mmdc -i $FLOWS_DIR/user_flow/happyflow-1/happyflow-1.mmd -o $FLOWS_DIR/user_flow/happyflow-1/happyflow-1.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-2/happyflow-2.mmd -o $FLOWS_DIR/user_flow/happyflow-2/happyflow-2.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-3/happyflow-3.mmd -o $FLOWS_DIR/user_flow/happyflow-3/happyflow-3.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-4/happyflow-4.mmd -o $FLOWS_DIR/user_flow/happyflow-4/happyflow-4.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-5/happyflow-5.mmd -o $FLOWS_DIR/user_flow/happyflow-5/happyflow-5.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-6/happyflow-6.mmd -o $FLOWS_DIR/user_flow/happyflow-6/happyflow-6.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-7/happyflow-7.mmd -o $FLOWS_DIR/user_flow/happyflow-7/happyflow-7.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-8/happyflow-8.mmd -o $FLOWS_DIR/user_flow/happyflow-8/happyflow-8.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-9/happyflow-9.mmd -o $FLOWS_DIR/user_flow/happyflow-9/happyflow-9.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-10/happyflow-10.mmd -o $FLOWS_DIR/user_flow/happyflow-10/happyflow-10.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-11/happyflow-11.mmd -o $FLOWS_DIR/user_flow/happyflow-11/happyflow-11.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-12/happyflow-12.mmd -o $FLOWS_DIR/user_flow/happyflow-12/happyflow-12.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-13/happyflow-13.mmd -o $FLOWS_DIR/user_flow/happyflow-13/happyflow-13.png &

wait
