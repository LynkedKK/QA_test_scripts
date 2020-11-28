import random
from pprint import pprint

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

from stubs.server.assign_table.assign_table_by_name import assignTableByName

import restaurant_manage.order_page

def run_check(json_metadata, r_browser, time_to_tap=4):
  TEST_ERR_MSG='test failed at TID_043'

  assertCheckPoint(r_browser, 'TID_043_1', TEST_ERR_MSG)

  order_page_po = restaurant_manage.order_page.Main(r_browser)


  for i in range(0,time_to_tap):
    # tap to let 1/all appears
    order_page_po.tapTopMostOrder()
    assertCheckPoint(r_browser, 'TID_043_2_{}'.format(i), TEST_ERR_MSG)
    order_page_po.tapTopMostOrderOneDelivered()
    assertCheckPoint(r_browser, 'TID_043_2_{}'.format(i), TEST_ERR_MSG)

  json_metadata['TID_043'] = 'passed'
