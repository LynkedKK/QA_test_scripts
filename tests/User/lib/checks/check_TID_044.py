import random
from pprint import pprint

import lib.pages.please_take_seat_first_dialogue as please_take_seat_first_dialogue
import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import assertCheckPoint

from stubs.server.assign_table.assign_table_by_name import assignTableByName

import lib.pages.restaurant_manage.order_page as order_page

def run_check(json_metadata, r_browser, table_number=38):
  TEST_ERR_MSG='test failed at TID_044'

  assertCheckPoint(r_browser, 'TID_044_1', TEST_ERR_MSG)

  order_page_po = order_page.Main(r_browser)
  order_page_po.longPressTopMostToShowDelete()

  assertCheckPoint(r_browser, 'TID_044_2', TEST_ERR_MSG)

  json_metadata['TID_044'] = 'passed'
