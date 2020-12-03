import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_028 import tour_TID_028 as tour_TID_028
import lib.checks.check_TID_030 as check_TID_030

def tour_TID_030(json_metadata):
  restaurant_manage_browser = tour_TID_028(json_metadata)

  check_TID_030.run_check(json_metadata, restaurant_manage_browser)

  return restaurant_manage_browser

  # assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,0.1,  'first time landing test after clicking accept failed')