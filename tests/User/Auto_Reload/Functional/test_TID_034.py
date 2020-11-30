import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_029 import tour_TID_029 as tour_TID_029
from Auto_Reload.Functional.test_TID_006 import tour_TID_006 as tour_TID_006

import lib.checks.check_TID_034 as check_TID_034

def tour_TID_034(json_metadata):
  # clear before test

  restaurant_manage_browser = tour_TID_029(json_metadata)
  client_browser = tour_TID_006(json_metadata)

  check_TID_034.run_check(json_metadata, restaurant_manage_browser, client_browser)

  return (restaurant_manage_browser, client_browser)
