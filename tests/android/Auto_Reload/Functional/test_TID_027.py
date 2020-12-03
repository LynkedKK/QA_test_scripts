import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_026 import tour_TID_026 as tour_TID_026
import lib.checks.check_TID_027 as check_TID_027
from lib.utils.save_recording_screen import saveRecordingScreen
from lib.utils.dismiss_test_device import dismissTestDevice

def test_TID_027(json_metadata):
  password_to_bruce=['xxxxxx']

  browser = tour_TID_026(json_metadata)

  try:

    for password in password_to_bruce:
      check_TID_027.run_check(json_metadata, browser, password)

  finally:
    saveRecordingScreen(browser,'TID_027_client')
    dismissTestDevice(browser)
