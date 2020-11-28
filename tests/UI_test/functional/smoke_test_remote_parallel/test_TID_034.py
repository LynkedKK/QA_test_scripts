import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *

from steps import *
from pages.config import *
from jp import *

from stubs.server.assign_table.assign_all_table import assignAllTable

from urls import *

from setupLocalChrome import *

from test_TID_029 import *
from test_TID_006 import *


def tour_TID_034(json_metadata):
  # clear before test

  restaurant_manage_browser = tour_TID_029(json_metadata)
  client_browser = tour_TID_006(json_metadata)

  check_TID_034.run_check(json_metadata, restaurant_manage_browser, client_browser)

  return (restaurant_manage_browser, client_browser)

  # assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,0.1,  'first time landing test after clicking accept failed')