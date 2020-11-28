import random
from pprint import pprint

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from stubs.server.assign_table.assign_table_by_name import assignTableByName

import restaurant_manage.bill_page



def run_check(json_metadata, browser):
  TEST_ERR_MSG='test failed at TID_050'

  assertCheckPoint(browser, 'TID_050_1', TEST_ERR_MSG)

  json_metadata['TID_050'] = 'passed'
