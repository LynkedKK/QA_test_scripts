import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from config import *
from time import sleep
from assert_check_point import assertCheckPoint

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
  sleep(5)
  assertCheckPoint(browser, 'TID_016_4', TEST_ERR_MSG, 0.055)


  food_menu_po.tapCartButton()
  assertCheckPoint(browser, 'TID_016_5', TEST_ERR_MSG)


  cart_page_po.tapRemoveButton(1)
  assertCheckPoint(browser, 'TID_016_6', TEST_ERR_MSG)

  json_metadata['TID_016'] = 'passed'
