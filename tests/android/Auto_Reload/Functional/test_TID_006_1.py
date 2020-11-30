import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_006 import tour_TID_006 as tour_TID_006
import lib.checks.check_TID_006_1 as check_TID_006_1

# assign table by stub
def tour_TID_006_1(json_metadata, username):
  browser = tour_TID_006(json_metadata, username)

  # check result
  check_TID_006_1.run_check(json_metadata, browser, username)

  return browser