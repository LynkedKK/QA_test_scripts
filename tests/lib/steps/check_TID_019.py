import please_take_seat_first_dialogue
import cart_page
# import item_add_page

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  TEST_ERR_MSG='It should send order successfully'

  # cart_page_po = cart_page.Main(browser)
  # please_take_seat_first_dialogue_po=please_take_seat_first_dialogue.Main(browser)
  # item_add_page_po=item_add_page.Main(browser)

  # check if red dialogue appears
  assertCheckPoint(browser, 'TID_019_1', TEST_ERR_MSG)
  sleep(0.5)

  # cart_page_po.tapPlaceOrderButton()
  # tap ok to dismiss dialogue
  # please_take_seat_first_dialogue_po.tapOkButtonOnDialogue()

  json_metadata['TID_019'] = 'passed'