import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_036 import tour_TID_036 as tour_TID_036
import lib.checks.check_TID_037 as check_TID_037

def tour_TID_037(json_metadata, table_num=37):
  # clear before test

  (r_browser, c_browser) = tour_TID_036(json_metadata, table_num)

  # perform check
  check_TID_037.run_check(json_metadata, r_browser, c_browser, table_num)

  return (r_browser, c_browser)
