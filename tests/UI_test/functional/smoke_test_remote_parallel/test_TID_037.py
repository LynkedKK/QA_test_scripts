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

from test_TID_036 import *
from check_TID_009 import *

import table_assigned_dialogue

def tour_TID_037(json_metadata, table_num=37):
  # clear before test

  (r_browser, c_browser) = tour_TID_036(json_metadata, table_num)

  table_assigned_dialogue_po = table_assigned_dialogue.Main(c_browser)
  table_assigned_dialogue_po.tapOkButtonOnDialogue()

  # check_TID_009.run_check(json_metadata, c_browser)
  check_TID_009.run_check(json_metadata, c_browser, 1)
  check_TID_012.run_check(json_metadata, c_browser)
  check_TID_013.run_check(json_metadata, c_browser)
  check_TID_017.run_check(json_metadata, c_browser)

  # goto order page
  check_TID_031.run_check(json_metadata, r_browser)

  # perform check
  check_TID_037.run_check(json_metadata, r_browser, c_browser, table_num)

  return (r_browser, c_browser)
