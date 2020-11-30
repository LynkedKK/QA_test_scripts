import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  TEST_ERR_MSG='It should send order successfully'
  cart_page_po = cart_page.Main(browser)

  assertCheckPoint(browser, 'TID_017_1', TEST_ERR_MSG)

  cart_page_po.tapPlaceOrderButton()

  assertCheckPoint(browser, 'TID_017_2', TEST_ERR_MSG)

  json_metadata['TID_017'] = 'passed'