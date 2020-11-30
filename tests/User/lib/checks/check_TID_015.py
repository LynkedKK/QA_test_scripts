import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  TEST_ERR_MSG='error during running test 015'
  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)

  assertCheckPoint(browser, 'TID_015_1', TEST_ERR_MSG)
  for i in range(1,20):
    cart_page_po.tapMinusButton(1)


  assertCheckPoint(browser, 'TID_015_2', TEST_ERR_MSG)

  json_metadata['TID_015'] = 'passed'
