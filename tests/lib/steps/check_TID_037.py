import random
from pprint import pprint

import please_take_seat_first_dialogue
import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from config import *
from time import sleep
from assert_check_point import assertCheckPoint

from stubs.server.assign_table.assign_table_by_name import assignTableByName

import restaurant_manage.admin_page
import restaurant_manage.order_page

def run_check(json_metadata, r_browser, c_browser, table_number=37):
  TEST_ERR_MSG='test failed at TID_037'

  assertCheckPoint(r_browser, 'TID_037_1', TEST_ERR_MSG)

  admin_page_with_site_nav_po = restaurant_manage.order_page.Main(r_browser)
  admin_page_with_site_nav_po.inputTableFilter(table_number)

  assertCheckPoint(r_browser, 'TID_037_2', TEST_ERR_MSG)

  json_metadata['TID_037'] = 'passed'
