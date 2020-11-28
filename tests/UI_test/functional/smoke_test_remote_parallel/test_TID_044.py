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

from test_TID_037 import *

def test_TID_044(json_metadata):
  # clear before test

  (r_browser, c_browser) = tour_TID_037(json_metadata, '44')

  # perform check
  check_TID_044.run_check(json_metadata, r_browser, 44)

  return (r_browser, c_browser)
