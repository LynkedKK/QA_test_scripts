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

from test_TID_046 import *

def test_TID_048(json_metadata, table_num=41, food_quantity=5):
  # clear before test

  (r_browser, c_browser) = tour_TID_046(json_metadata, table_num, food_quantity)

  check_TID_032.run_check(json_metadata, r_browser)

  check_TID_048.run_check(json_metadata, r_browser, table_num)

  return (r_browser, c_browser)
