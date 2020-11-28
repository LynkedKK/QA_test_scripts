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

from test_TID_035 import *

def tour_TID_036(json_metadata, table_num='TID_036'):
  # clear before test

  (r_browser, c_browser) = tour_TID_035(json_metadata)

  check_TID_036.run_check(json_metadata, r_browser, c_browser, table_num)


  return (r_browser, c_browser)
