import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_037 import tour_TID_037 as tour_TID_037
import lib.checks.check_TID_038 as check_TID_038
from lib.utils.save_recording_screen import saveRecordingScreen
from lib.utils.dismiss_test_device import dismissTestDevice

def test_TID_038(json_metadata):
  # clear before test

  (r_browser, c_browser) = tour_TID_037(json_metadata, '38')

  try:

    check_TID_038.run_check(json_metadata, r_browser, 38)

  finally:
    saveRecordingScreen(r_browser,'TID_004_client')
    saveRecordingScreen(c_browser,'TID_004_client')

    dismissTestDevice(r_browser)
    dismissTestDevice(c_browser)
