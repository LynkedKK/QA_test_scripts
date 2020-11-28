import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from config import *
from time import sleep
from assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  TEST_ERR_MSG='error during running test 015'
  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)

  assertCheckPoint(browser, 'TID_015_1', TEST_ERR_MSG)
  for i in range(1,20):
    cart_page_po.tapMinusButton(1)


  assertCheckPoint(browser, 'TID_015_2', TEST_ERR_MSG)

  json_metadata['TID_015'] = 'passed'
