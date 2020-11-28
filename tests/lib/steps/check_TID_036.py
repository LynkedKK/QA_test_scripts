import random
from pprint import pprint
from time import sleep

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

from stubs.server.assign_table.assign_table_by_name import assignTableByName

import restaurant_manage.admin_page

def run_check(json_metadata, r_browser, c_browser, assign_table='let say any table number test'):
  TEST_ERR_MSG='test failed at TID_036'


  assertCheckPoint(r_browser, 'TID_036_1', TEST_ERR_MSG)
  assertCheckPoint(c_browser, 'TID_036_2', TEST_ERR_MSG)

  admin_page_with_site_nav_po = restaurant_manage.admin_page.Main(r_browser)
  admin_page_with_site_nav_po.assignTable(assign_table)
  admin_page_with_site_nav_po.assignTableSubmit()

  assertCheckPoint(r_browser, 'TID_036_3', TEST_ERR_MSG)

  sleep(15)

  assertCheckPoint(c_browser, 'TID_036_4', TEST_ERR_MSG)

  json_metadata['TID_036'] = 'passed'
