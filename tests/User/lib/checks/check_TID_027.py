import random
from pprint import pprint

from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import assertCheckPoint

import lib.pages.restaurant_manage.password as password

def run_check(json_metadata, browser, password_to_bruce):
  TEST_ERR_MSG='test failed at TID_027'

  assertCheckPoint(browser, 'TID_027_1', TEST_ERR_MSG)

  restaurant_mgmt_po = password.Main(browser)
  restaurant_mgmt_po.inputPassword(password_to_bruce)
  restaurant_mgmt_po.tapLogin()

  assertCheckPoint(browser, 'TID_027_2_{}'.format(password_to_bruce), TEST_ERR_MSG)

  json_metadata['TID_027'] = 'passed'
