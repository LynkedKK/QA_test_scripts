import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_045 import tour_TID_045 as tour_TID_045
import lib.checks.check_TID_046 as check_TID_046

def tour_TID_046(json_metadata, table_num=41, food_quantity=5):
  # clear before test

  (r_browser, c_browser) = tour_TID_045(json_metadata, table_num, food_quantity)

  check_TID_046.run_check(json_metadata, r_browser)

  return (r_browser, c_browser)
