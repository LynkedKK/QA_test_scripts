import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import *

def run_check(json_metadata, browser, food_item_idx=1):
  TEST_ERR_MSG='It should direct to item add page'

  assertCheckPoint(browser, 'TID_009_1', TEST_ERR_MSG)

  food_menu_po = food_menu.Main(browser)
  food_menu_po.tapFoodItemByIdx(food_item_idx)

  assertCheckPoint(browser, 'TID_009_2', TEST_ERR_MSG)
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

  json_metadata['TID_009'] = 'passed'
