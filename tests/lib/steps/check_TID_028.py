import random
from pprint import pprint

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

import restaurant_manage.password

def run_check(json_metadata, browser, correct_password):
  TEST_ERR_MSG='test failed at TID_028'

  assertCheckPoint(browser, 'TID_028_1', TEST_ERR_MSG)

  restaurant_mgmt_po = restaurant_manage.password.Main(browser)
  restaurant_mgmt_po.inputPassword(correct_password)
  restaurant_mgmt_po.tapLogin()

  assertCheckPoint(browser, 'TID_028_2_{}'.format(correct_password), TEST_ERR_MSG)

  json_metadata['TID_028'] = 'passed'
