import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_040 import tour_TID_040 as tour_TID_040
import lib.checks.check_TID_042 as check_TID_042

from lib.utils.save_recording_screen import saveRecordingScreen
from lib.utils.dismiss_test_device import dismissTestDevice

def test_TID_042(json_metadata, table_num=41):
  (r_browser, c_browser) = tour_TID_040(json_metadata, table_num, 5)

  try:
    # clear before test

    check_TID_042.run_check(json_metadata, r_browser, table_num)

  finally:
    saveRecordingScreen(r_browser,'TID_042_restaurant')
    dismissTestDevice(r_browser)
    dismissTestDevice(c_browser)
