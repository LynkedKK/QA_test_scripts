import os,sys

CURR_DIR=os.path.dirname(__file__)
USER_TEST_DIR=os.path.abspath(os.path.join(CURR_DIR,'..','..'))
LIB_DIR=os.path.abspath(os.path.join(USER_TEST_DIR,'lib'))

ASSERTS_DIR=os.path.abspath(os.path.join(LIB_DIR,'asserts'))
STEPS_DIR=os.path.abspath(os.path.join(LIB_DIR,'steps'))
TICKETS_DIR=os.path.abspath(os.path.join(LIB_DIR,'tickets'))
# TOURS_DIR=os.path.abspath(os.path.join(LIB_DIR,'tours'))
CHECKS_DIR=os.path.abspath(os.path.join(LIB_DIR,'checks'))
PAGES_DIR=os.path.abspath(os.path.join(LIB_DIR,'pages'))

UTILS_DIR=os.path.abspath(os.path.join(LIB_DIR,'utils'))

sys.path.append(LIB_DIR)
sys.path.append(ASSERTS_DIR)
sys.path.append(STEPS_DIR)
sys.path.append(TICKETS_DIR)
# sys.path.append(TOURS_DIR)
sys.path.append(CHECKS_DIR)
sys.path.append(PAGES_DIR)
sys.path.append(UTILS_DIR)

assert False, 'hello fail'