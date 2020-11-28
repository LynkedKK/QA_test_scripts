import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from config import *
from time import sleep
from assert_check_point import assertCheckPoint

def run_check(json_metadata, browser, food_idx=1):
  TEST_ERR_MSG='It should increase the quantity of the food item'

  # line_up_po = line_up_page.Main(browser)
  # dialogue_po= line_up_confirmation_dialogue.Main(browser)
  item_add_page_po = item_add_page.Main(browser)

  assertCheckPoint(browser, 'TID_012_1_{}'.format(food_idx), TEST_ERR_MSG)
  item_add_page_po.tapAddIntoCartButton()

  # sleep to let dialogue gone
  sleep(3)

  assertCheckPoint(browser, 'TID_012_2_{}'.format(food_idx), TEST_ERR_MSG, 0.06)

  json_metadata['TID_012'] = 'passed'