import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_017 import tour_TID_017 as tour_TID_017
import lib.checks.check_TID_019 as check_TID_019

def tour_TID_019(json_metadata, username="TID_019"):

  browser = tour_TID_017(json_metadata, username)

  # the update of line up info appears here
  check_TID_019.run_check(json_metadata, browser)

  return browser
