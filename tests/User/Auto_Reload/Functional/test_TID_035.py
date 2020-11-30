import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_034 import tour_TID_034 as tour_TID_034
import lib.checks.check_TID_035 as check_TID_035

def tour_TID_035(json_metadata):
  # clear before test

  (r_browser, c_browser) = tour_TID_034(json_metadata)

  check_TID_035.run_check(json_metadata, r_browser, c_browser)

  return (r_browser, c_browser)
