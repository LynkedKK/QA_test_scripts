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
  TEST_ERR_MSG='test failed at TID_049'

  assertCheckPoint(browser, 'TID_049_1', TEST_ERR_MSG)
  bill_page_po = restaurant_manage.bill_page.Main(browser)
  bill_page_po.tapCheckOutBill()

  alert = WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())
  text = alert.text
  alert.accept()

  assertCheckPoint(browser, 'TID_049_2', TEST_ERR_MSG)


  json_metadata['TID_049'] = 'passed'
