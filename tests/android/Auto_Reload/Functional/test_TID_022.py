import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_012 import tour_TID_012 as tour_TID_012
import lib.checks.check_TID_022 as check_TID_022

def tour_TID_022(json_metadata, username="TID_022"):

  browser = tour_TID_012(json_metadata, username)

  # the update of line up info appears here
  check_TID_022.run_check(json_metadata, browser)

  return browser
