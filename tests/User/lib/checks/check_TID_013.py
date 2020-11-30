import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import *

def run_check(json_metadata, browser):
  TEST_ERR_MSG='It should increase the quantity of the food item'

  food_menu_po=food_menu.Main(browser)

  assertCheckPoint(browser, 'TID_013_1', TEST_ERR_MSG)
  food_menu_po.tapCartButton()

  assertCheckPoint(browser, 'TID_013_2', TEST_ERR_MSG)

  json_metadata['TID_013'] = 'passed'