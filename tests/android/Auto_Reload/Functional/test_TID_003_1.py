import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__))
from lib.config import *
from urls import *

from lib.asserts.assert_check_point import *
from lib.utils.close_appium_session import *
from lib.steps.create_appium_instance import *
from lib.utils.get_current_test import *

from Auto_Reload.Functional.test_TID_001 import tour_TID_001 as tour_TID_001
import lib.checks.check_TID_003 as check_TID_003

def tour_TID_003_1(json_metadata):
  browser = tour_TID_001(json_metadata)

  # check result
  check_TID_003.run_check(json_metadata, browser)

  return browser