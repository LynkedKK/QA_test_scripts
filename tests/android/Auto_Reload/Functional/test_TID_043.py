import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_041 import tour_TID_041 as tour_TID_041
import lib.checks.check_TID_043 as check_TID_043
from lib.utils.dismiss_test_device import *
from lib.utils.save_recording_screen import saveRecordingScreen
from lib.utils.dismiss_test_device import dismissTestDevice

def test_TID_043(json_metadata, table_num=43, food_quantity=5):
  (r_browser, c_browser) = tour_TID_041(json_metadata, table_num, food_quantity)

  try:
    # clear before test

    check_TID_043.run_check(json_metadata, r_browser,  food_quantity-1)

    return (r_browser, c_browser)

  finally:
    saveRecordingScreen(r_browser,'TID_043_restaurant')
    saveRecordingScreen(c_browser,'TID_043_client')

    dismissTestDevice(r_browser)
    dismissTestDevice(c_browser)