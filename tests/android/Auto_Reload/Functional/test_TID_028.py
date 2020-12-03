import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_026 import tour_TID_026 as tour_TID_026
import lib.checks.check_TID_028 as check_TID_028

def tour_TID_028(json_metadata):
  correct_password=['999999']

  restaurant_manage_browser = tour_TID_026(json_metadata)

  for password in correct_password:
    check_TID_028.run_check(json_metadata, restaurant_manage_browser, password)

  return restaurant_manage_browser

  # assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,0.1,  'first time landing test after clicking accept failed')
