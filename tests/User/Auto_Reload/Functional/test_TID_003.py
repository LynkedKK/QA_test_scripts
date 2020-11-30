import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__))
from lib.config import *
from urls import *

from lib.steps.create_appium_instance import *
from lib.asserts.assert_check_point import *
from lib.utils.close_appium_session import *

from Auto_Reload.Functional.test_TID_002 import tour_TID_002 as tour_TID_002
import lib.checks.check_TID_003 as check_TID_003
from lib.utils.save_recording_screen import saveRecordingScreen

def tour_TID_003(json_metadata):
  browser = tour_TID_002(json_metadata)

  check_TID_003.run_check(json_metadata, browser)


  return browser
