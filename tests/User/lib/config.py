import os,sys

CURR_DIR=os.path.dirname(__file__)
LIB_DIR=CURR_DIR
TEST_HOME=os.path.abspath(LIB_DIR+'/..')
REPORT_DIR=os.path.abspath(TEST_HOME+'/reports')
REPORT_ASSET_DIR=os.path.abspath(REPORT_DIR+'/assets')
RECORDING_DIR=os.path.abspath(REPORT_ASSET_DIR+'/recordings')

SCREENCAPTURE_DIR=REPORT_ASSET_DIR
VIDEO_PATH=RECORDING_DIR

# ASSERTS_DIR=os.path.abspath(os.path.join(LIB_DIR,'asserts'))
# STEPS_DIR=os.path.abspath(os.path.join(LIB_DIR,'steps'))
# TICKETS_DIR=os.path.abspath(os.path.join(LIB_DIR,'tickets'))
# # TOURS_DIR=os.path.abspath(os.path.join(LIB_DIR,'tours'))
# CHECKS_DIR=os.path.abspath(os.path.join(LIB_DIR,'checks'))
# PAGES_DIR=os.path.abspath(os.path.join(LIB_DIR,'pages'))

# UTILS_DIR=os.path.abspath(os.path.join(LIB_DIR,'utils'))

sys.path.append(LIB_DIR)
# sys.path.append(ASSERTS_DIR)
# sys.path.append(STEPS_DIR)
# sys.path.append(TICKETS_DIR)
# # sys.path.append(TOURS_DIR)
# sys.path.append(CHECKS_DIR)
# sys.path.append(PAGES_DIR)
# sys.path.append(UTILS_DIR)
