import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_013 import tour_TID_013 as tour_TID_013
import lib.checks.check_TID_014 as check_TID_014

def tour_TID_014(json_metadata, username="TID_009"):

  browser = tour_TID_013(json_metadata, username)

  # the update of line up info appears here
  check_TID_014.run_check(json_metadata, browser)

  return browser
