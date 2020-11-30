import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_009 import tour_TID_009 as tour_TID_009
import lib.checks.check_TID_012 as check_TID_012

def tour_TID_012(json_metadata, username=__name__):

  browser = tour_TID_009(json_metadata,username)

  # the update of line up info appears here
  check_TID_012.run_check(json_metadata, browser)

  return browser
