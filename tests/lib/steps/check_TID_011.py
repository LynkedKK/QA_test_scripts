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

  # line_up_po = line_up_page.Main(browser)
  # dialogue_po= line_up_confirmation_dialogue.Main(browser)
  item_add_page_po = item_add_page.Main(browser)

  assertCheckPoint(browser, 'TID_011_1', TEST_ERR_MSG)
  item_add_page_po.removeFood()

  assertCheckPoint(browser, 'TID_011_2', TEST_ERR_MSG)

  json_metadata['TID_011'] = 'passed'