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

from test_TID_034 import *

def tour_TID_035(json_metadata):
  # clear before test

  (r_browser, c_browser) = tour_TID_034(json_metadata)

  check_TID_035.run_check(json_metadata, r_browser, c_browser)

  return (r_browser, c_browser)
