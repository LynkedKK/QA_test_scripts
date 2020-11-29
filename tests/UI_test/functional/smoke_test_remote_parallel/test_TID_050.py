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

from urls import *

from setupLocalChrome import *

from test_TID_049 import *

def test_TID_050(json_metadata, table_num=50, food_quantity=5):
  # clear before test

  (r_browser, c_browser) = tour_TID_049(json_metadata, table_num, food_quantity)

  # r_browser = setupLocalChrome()
  c_browser.get(LINE_UP_PAGE)

  check_TID_050.run_check(json_metadata, c_browser)

  return (r_browser, c_browser)
