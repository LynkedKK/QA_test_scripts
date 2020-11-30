
import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *
from lib.urls import *

from Auto_Reload.Functional.test_TID_049 import tour_TID_049 as tour_TID_049
import lib.checks.check_TID_050 as check_TID_050
from lib.utils.dismiss_test_device import *
from lib.utils.save_recording_screen import saveRecordingScreen

def test_TID_050(json_metadata, table_num=50, food_quantity=5):
  # clear before test

  (r_browser, c_browser) = tour_TID_049(json_metadata, table_num, food_quantity)

  try:

    c_browser.get(LINE_UP_PAGE)

    check_TID_050.run_check(json_metadata, c_browser)

  finally:
    saveRecordingScreen(r_browser,'TID_050_restaurant')
    dismissTestDevice(r_browser)

    saveRecordingScreen(c_browser,'TID_050_client')
    dismissTestDevice(c_browser)
