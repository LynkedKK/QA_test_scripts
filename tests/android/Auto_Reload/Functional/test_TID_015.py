import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_014 import tour_TID_014 as tour_TID_014
import lib.checks.check_TID_015 as check_TID_015
from lib.utils.save_recording_screen import saveRecordingScreen
from lib.utils.dismiss_test_device import dismissTestDevice

def test_TID_015(json_metadata, username="TID_015"):

  browser = tour_TID_014(json_metadata, username)

  try:

    check_TID_015.run_check(json_metadata, browser)

  finally:
    saveRecordingScreen(browser,'TID_015_client')

    dismissTestDevice(browser)
