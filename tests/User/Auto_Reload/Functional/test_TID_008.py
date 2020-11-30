import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_006 import tour_TID_006 as tour_TID_006
import lib.checks.check_TID_008 as check_TID_008
from lib.utils.save_recording_screen import saveRecordingScreen
from lib.utils.dismiss_test_device import dismissTestDevice

def test_TID_008(json_metadata):
  browser = tour_TID_006(json_metadata)

  try:

    check_TID_008.run_check(json_metadata, browser)

  finally:
    saveRecordingScreen(browser,'TID_008_client')

    dismissTestDevice(browser)
