import random
from pprint import pprint

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

from stubs.server.assign_table.assign_table_by_name import assignTableByName

import restaurant_manage.order_page

def run_check(json_metadata, r_browser, table_number=38):
  TEST_ERR_MSG='test failed at TID_041'

  assertCheckPoint(r_browser, 'TID_041_1', TEST_ERR_MSG)

  order_page_po = restaurant_manage.order_page.Main(r_browser)

  # tap to let 1/all appears
  order_page_po.tapTopMostOrder()
  assertCheckPoint(r_browser, 'TID_041_2', TEST_ERR_MSG)

  order_page_po.tapTopMostOrderOneDelivered()
  assertCheckPoint(r_browser, 'TID_041_3', TEST_ERR_MSG)

  json_metadata['TID_041'] = 'passed'
