import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *
from setupLocalChrome import *

from steps import *
from pages.config import *
from jp import *

def tour_TID_001(json_metadata):

  browser = setupLocalChrome()

  check_TID_001.run_check(json_metadata, browser)

  return browser
