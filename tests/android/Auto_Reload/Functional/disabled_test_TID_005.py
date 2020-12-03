import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_003_1 import tour_TID_003_1 as tour_TID_003_1
import lib.checks.check_TID_005 as check_TID_005

def tour_TID_005(json_metadata):
  browser = tour_TID_003_1(json_metadata)

  # check result
  check_TID_005.run_check(json_metadata, browser)

  return browser