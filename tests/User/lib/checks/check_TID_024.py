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

def run_check(json_metadata, browser):
  TEST_ERR_MSG='test failed at TID_024'
  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)
  item_add_page_po=item_add_page.Main(browser)

  # please_take_seat_first_dialogue_po=please_take_seat_first_dialogue.Main(browser)
  # item_add_page_po=item_add_page.Main(browser)

  assertCheckPoint(browser, 'TID_024_1', TEST_ERR_MSG)
  sleep(0.5)

  # tap ok to dismiss dialogue
  # please_take_seat_first_dialogue_po.tapOkButtonOnDialogue()

  assertCheckPoint(browser, 'TID_024_2', TEST_ERR_MSG)

  json_metadata['TID_024'] = 'passed'
