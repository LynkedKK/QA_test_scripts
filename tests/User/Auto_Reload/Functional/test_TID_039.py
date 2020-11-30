import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_036 import tour_TID_036 as tour_TID_036

import lib.pages.table_assigned_dialogue as table_assigned_dialogue
import lib.checks.check_TID_009 as check_TID_009
import lib.checks.check_TID_010 as check_TID_010
import lib.checks.check_TID_012 as check_TID_012
import lib.checks.check_TID_013 as check_TID_013
import lib.checks.check_TID_017 as check_TID_017
import lib.checks.check_TID_031 as check_TID_031
import lib.checks.check_TID_037 as check_TID_037
import lib.checks.check_TID_039 as check_TID_039

def tour_TID_039(json_metadata, table_num=37, food_quantity=5):
  # clear before test

  (r_browser, c_browser) = tour_TID_036(json_metadata, table_num)

  table_assigned_dialogue_po = table_assigned_dialogue.Main(c_browser)
  table_assigned_dialogue_po.tapOkButtonOnDialogue()

  # check_TID_009.run_check(json_metadata, c_browser)
  check_TID_009.run_check(json_metadata, c_browser, 1)


  # default will add one, this is the number of times for "+" to press
  for i in range(0,food_quantity-1):
    check_TID_010.run_check(json_metadata, c_browser)

  check_TID_012.run_check(json_metadata, c_browser)
  check_TID_013.run_check(json_metadata, c_browser)

  check_TID_017.run_check(json_metadata, c_browser)

  # goto order page
  check_TID_031.run_check(json_metadata, r_browser)

  # perform check
  check_TID_037.run_check(json_metadata, r_browser, c_browser, table_num)

  check_TID_039.run_check(json_metadata, r_browser)

  return (r_browser, c_browser)
