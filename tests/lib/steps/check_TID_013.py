import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from config import *
from time import sleep
from assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  TEST_ERR_MSG='It should increase the quantity of the food item'

  food_menu_po=food_menu.Main(browser)

  assertCheckPoint(browser, 'TID_013_1', TEST_ERR_MSG)
  food_menu_po.tapCartButton()

  assertCheckPoint(browser, 'TID_013_2', TEST_ERR_MSG)

  json_metadata['TID_013'] = 'passed'