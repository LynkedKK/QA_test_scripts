import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_019 import tour_TID_019 as tour_TID_019
import lib.checks.check_TID_021 as check_TID_021
from lib.utils.save_recording_screen import saveRecordingScreen
from lib.utils.dismiss_test_device import dismissTestDevice

def te1st_TID_021(json_metadata, username="TID_021"):
  browser = tour_TID_019(json_metadata, username)

  try:

    check_TID_021.run_check(json_metadata, browser)

  finally:
    saveRecordingScreen(browser,'TID_021_client')

    dismissTestDevice(browser)
