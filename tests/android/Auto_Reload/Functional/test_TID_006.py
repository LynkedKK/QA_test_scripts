import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_003 import tour_TID_003 as tour_TID_003
import lib.checks.check_TID_006 as check_TID_006
from lib.utils.save_recording_screen import saveRecordingScreen

def tour_TID_006(json_metadata, username='TID_006'):
  browser = tour_TID_003(json_metadata)

  # check result
  check_TID_006.run_check(json_metadata, browser, username)

  return browser
