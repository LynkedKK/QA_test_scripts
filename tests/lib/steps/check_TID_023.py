import random
from pprint import pprint

import please_take_seat_first_dialogue
import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page

import order_history_page

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

from stubs.server.assign_table.assign_table_by_name import assignTableByName

def run_check(json_metadata, browser, number_of_people=1):
  TEST_ERR_MSG='test failed at TID_023'
  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)
  item_add_page_po=item_add_page.Main(browser)

  # please_take_seat_first_dialogue_po=please_take_seat_first_dialogue.Main(browser)
  # item_add_page_po=item_add_page.Main(browser)

  assertCheckPoint(browser, 'TID_023_1', TEST_ERR_MSG)
  sleep(0.5)

  order_history_with_order_po = order_history_page.WithOrder(browser)
  order_history_with_order_po.updateNumberOfPeople(number_of_people)

  # tap ok to dismiss dialogue
  # please_take_seat_first_dialogue_po.tapOkButtonOnDialogue()

  assertCheckPoint(browser, 'TID_023_2', TEST_ERR_MSG)

  json_metadata['TID_023'] = 'passed'
