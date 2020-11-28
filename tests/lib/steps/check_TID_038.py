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

import restaurant_manage.order_page

def run_check(json_metadata, r_browser, table_number=38):
  TEST_ERR_MSG='test failed at TID_038'

  assertCheckPoint(r_browser, 'TID_038_1', TEST_ERR_MSG)

  order_page_po = restaurant_manage.order_page.Main(r_browser)
  order_page_po.tapTopMostOrder()

  assertCheckPoint(r_browser, 'TID_038_2', TEST_ERR_MSG)

  json_metadata['TID_038'] = 'passed'
