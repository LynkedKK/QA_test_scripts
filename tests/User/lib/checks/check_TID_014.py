import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *

from time import sleep

from lib.asserts.assert_check_point import assertCheckPoint

def run_check(json_metadata, browser, things_to_add=14):
  TEST_ERR_MSG='TID_014 failed'
  cart_page_po = cart_page.Main(browser)

  cart_page_po.tapBottomBarCartButton()

  assertCheckPoint(browser, 'TID_014_1', TEST_ERR_MSG)
  for i in range(1,things_to_add):
    cart_page_po.tapAddButton(1)
    sleep(0.05)

  assertCheckPoint(browser, 'TID_014_2', TEST_ERR_MSG)

  json_metadata['TID_014'] = 'passed'