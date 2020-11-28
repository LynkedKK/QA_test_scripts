import os,sys
from pprint import pprint
import random
from time import sleep

TEST_DIR=os.path.dirname(__file__)
FUNCTIONAL_DIR=os.path.abspath(TEST_DIR+'/..')
UI_TEST_DIR=os.path.abspath(FUNCTIONAL_DIR+'/..')
TEST_ROOT=os.path.abspath(UI_TEST_DIR+'/..')
LIB_DIR=os.path.abspath(TEST_ROOT+'/lib')
LIB_PO_DIR=os.path.abspath(LIB_DIR+'/pages')
LIB_ELE_DIR=os.path.abspath(LIB_DIR+'./elements')
LANG_DIR=os.path.abspath(TEST_ROOT+'/lang')
LIB_CONFIG_DIR=os.path.abspath(LIB_DIR+'/configs')
LIB_ASSERT_DIR=os.path.abspath(LIB_DIR+'/asserts')
LIB_STEPS_DIR=os.path.abspath(LIB_DIR+'/steps')

LIB_STUBS_DIR=os.path.abspath(LIB_DIR+'/stubs')
LIB_STUBS_SERVER_DIR=os.path.abspath(LIB_STUBS_DIR+'/server')

sys.path.append(LIB_DIR)
sys.path.append(LIB_PO_DIR)
sys.path.append(LANG_DIR)
sys.path.append(LIB_CONFIG_DIR)
sys.path.append(LIB_ASSERT_DIR)
sys.path.append(LIB_STEPS_DIR)
sys.path.append(LIB_STUBS_DIR)
sys.path.append(TEST_DIR)

from steps import *

# packed steps




from jp import *

from stubs.server.assign_table.assign_table_by_name import assignTableByName

SELENIUM_HUB_HOST='localhost'

# todo: factorize me
from urls import *
LINE_UP_PAGE='http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/?do_lineup'
FOOD_MENU_PAGE='http://menymeny.com/food/やきとり/'

from setupLocalChrome import *

from test_TID_028 import *

def tour_TID_033(json_metadata):
  restaurant_manage_browser = tour_TID_028(json_metadata)

  check_TID_033.run_check(json_metadata, restaurant_manage_browser)

  return restaurant_manage_browser

  # assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,0.1,  'first time landing test after clicking accept failed')