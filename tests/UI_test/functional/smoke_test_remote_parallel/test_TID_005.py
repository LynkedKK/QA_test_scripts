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

from test_TID_003_1 import *

FOOD_MENU_PAGE='http://menymeny.com/food/やきとり/'
MAIN_MENU_PAGE=FOOD_MENU_PAGE

# TODO: need to clear flow
def test_TID_005(json_metadata):

  browser = tour_TID_003_1(json_metadata)

  # check result
  # FLEXIBILITY: the landing may follow the entry point
  browser.get(MAIN_MENU_PAGE)
  check_TID_005.run_check(json_metadata, browser)

  browser.quit()

  # assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,0.1,  'first time landing test after clicking accept failed')