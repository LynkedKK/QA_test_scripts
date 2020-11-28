import please_take_seat_first_dialogue
import food_menu
import cart_page
# import item_add_page

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  TEST_ERR_MSG='It should send order successfully'

  # please_take_seat_first_dialogue_po=please_take_seat_first_dialogue.Main(browser)
  # item_add_page_po=item_add_page.Main(browser)

  assertCheckPoint(browser, 'TID_022_1', TEST_ERR_MSG)
  # sleep(0.5)
  fm_page_po= food_menu.Main(browser)
  fm_page_po.tapCartButton()

  cart_page_po = cart_page.Main(browser)
  cart_page_po.tapPlaceOrderButton()

  cart_page_po.tapOrderhistoryIcon()

  # tap ok to dismiss dialogue
  # please_take_seat_first_dialogue_po.tapOkButtonOnDialogue()

  assertCheckPoint(browser, 'TID_022_2', TEST_ERR_MSG)

  json_metadata['TID_022'] = 'passed'
