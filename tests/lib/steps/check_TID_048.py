import random
from pprint import pprint

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

from stubs.server.assign_table.assign_table_by_name import assignTableByName

import restaurant_manage.order_page
import restaurant_manage.bill_page

def run_check(json_metadata, r_browser, table_num):
  TEST_ERR_MSG='test failed at TID_048'

  assertCheckPoint(r_browser, 'TID_048_1', TEST_ERR_MSG)
  bill_page_po= restaurant_manage.bill_page.Main(r_browser)
  bill_page_po.inputTableFilter(table_num)

  assertCheckPoint(r_browser, 'TID_048_2', TEST_ERR_MSG)


  json_metadata['TID_048'] = 'passed'
