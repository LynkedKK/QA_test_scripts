import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_012 import tour_TID_012 as tour_TID_012
import lib.checks.check_TID_013 as check_TID_013

def tour_TID_013(json_metadata, username=__name__):
  browser = tour_TID_012(json_metadata,username)

  check_TID_013.run_check(json_metadata, browser)

  return browser
