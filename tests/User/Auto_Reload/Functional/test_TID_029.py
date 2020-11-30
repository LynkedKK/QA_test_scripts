import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from lib.stubs.server.assign_table.assign_all_table import assignAllTable

# from setupLocalChrome import *
from Auto_Reload.Functional.test_TID_028 import tour_TID_028 as tour_TID_028
import lib.checks.check_TID_029 as check_TID_029

def tour_TID_029(json_metadata):
  assignAllTable('TID.*')

  restaurant_manage_browser = tour_TID_028(json_metadata)

  check_TID_029.run_check(json_metadata, restaurant_manage_browser)

  return restaurant_manage_browser

  # assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,0.1,  'first time landing test after clicking accept failed')