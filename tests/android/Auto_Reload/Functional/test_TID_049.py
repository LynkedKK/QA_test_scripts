import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_047 import tour_TID_047 as tour_TID_047
import lib.checks.check_TID_049 as check_TID_049

def tour_TID_049(json_metadata, table_num=41, food_quantity=5):
  # clear before test

  (r_browser, c_browser) = tour_TID_047(json_metadata, table_num, food_quantity)

  # r_browser = setupLocalChrome()
  # r_browser.get('http://menymeny.com/manage/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/?home=bill')

  check_TID_049.run_check(json_metadata, r_browser)

  return (r_browser, c_browser)
