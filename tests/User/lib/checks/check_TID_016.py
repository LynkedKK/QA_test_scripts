import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import assertCheckPoint

def run_check(json_metadata, browser, add_food_item_idx=2):
  TEST_ERR_MSG='test failed at TID_016'
  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)
  item_add_page_po=item_add_page.Main(browser)

  # escape from cart list page from 015
  # todo: remove me
  # cart_page_po.tapTopLeftCloseButton()
  # assertCheckPoint(browser, 'TID_016_1', TEST_ERR_MSG)

  # add another food
  cart_page_po.tapBottomBarMenuButton()
  food_menu_po.tapFoodItemByIdx(add_food_item_idx)
  assertCheckPoint(browser, 'TID_016_2', TEST_ERR_MSG)


  item_add_page_po.addFood()
  assertCheckPoint(browser, 'TID_016_3', TEST_ERR_MSG)


  item_add_page_po.tapAddIntoCartButton()
  assertCheckPoint(browser, 'TID_016_4', TEST_ERR_MSG)


  food_menu_po.tapCartButton()
  assertCheckPoint(browser, 'TID_016_5', TEST_ERR_MSG)


  cart_page_po.tapRemoveButton(1)
  assertCheckPoint(browser, 'TID_016_6', TEST_ERR_MSG)

  json_metadata['TID_016'] = 'passed'
