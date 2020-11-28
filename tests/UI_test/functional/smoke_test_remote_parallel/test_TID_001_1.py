import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *
from setupRemoteChrome import *

from steps import *
from pages.config import *
from jp import *

def tour_TID_001_1(json_metadata):

  browser = setupRemoteChrome()

  check_TID_001.run_check(json_metadata, browser)

  return browser
