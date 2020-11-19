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

mmdc -i $FLOWS_DIR/user_flow/happyflow-1/happy-flow-1.mmd -o $FLOWS_DIR/user_flow/happyflow-1/happy-flow-1.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-2/happy-flow-2.mmd -o $FLOWS_DIR/user_flow/happyflow-2/happy-flow-2.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-3/happy-flow-3.mmd -o $FLOWS_DIR/user_flow/happyflow-3/happy-flow-3.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-4/happy-flow-4.mmd -o $FLOWS_DIR/user_flow/happyflow-4/happy-flow-4.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-5/happy-flow-5.mmd -o $FLOWS_DIR/user_flow/happyflow-5/happy-flow-5.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-6/happy-flow-6.mmd -o $FLOWS_DIR/user_flow/happyflow-6/happy-flow-6.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-7/happy-flow-7.mmd -o $FLOWS_DIR/user_flow/happyflow-7/happy-flow-7.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-8/happy-flow-8.mmd -o $FLOWS_DIR/user_flow/happyflow-8/happy-flow-8.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-9/happy-flow-9.mmd -o $FLOWS_DIR/user_flow/happyflow-9/happy-flow-9.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-10/happy-flow-10.mmd -o $FLOWS_DIR/user_flow/happyflow-10/happy-flow-10.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-11/happy-flow-11.mmd -o $FLOWS_DIR/user_flow/happyflow-11/happy-flow-11.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-12/happy-flow-12.mmd -o $FLOWS_DIR/user_flow/happyflow-12/happy-flow-12.png &

mmdc -i $FLOWS_DIR/user_flow/happyflow-13/happy-flow-13.mmd -o $FLOWS_DIR/user_flow/happyflow-13/happy-flow-13.png &

wait
