import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_040 import tour_TID_040 as tour_TID_040
import lib.checks.check_TID_041 as check_TID_041

def tour_TID_041(json_metadata, table_num=41, food_quantity=5):
  # clear before test

  (r_browser, c_browser) = tour_TID_040(json_metadata, table_num, food_quantity)

  check_TID_041.run_check(json_metadata, r_browser, table_num)

  return (r_browser, c_browser)
