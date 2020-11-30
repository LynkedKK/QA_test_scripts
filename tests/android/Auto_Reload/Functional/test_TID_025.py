import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_023 import tour_TID_023 as tour_TID_023
import lib.checks.check_TID_025 as check_TID_025
from lib.utils.save_recording_screen import saveRecordingScreen
from lib.utils.dismiss_test_device import dismissTestDevice

def test_TID_025(json_metadata, username="TID_025", NUM_PEOPLE_TOTAL=5):
  browser = tour_TID_023(json_metadata, username)

  try:

    for i in range(1, NUM_PEOPLE_TOTAL+1):
      check_TID_025.run_check(json_metadata, browser,i)

  finally:
    saveRecordingScreen(browser,'TID_025_client')

    dismissTestDevice(browser)
