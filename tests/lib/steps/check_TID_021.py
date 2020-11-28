import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from config import *
from time import sleep
from assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  TEST_ERR_MSG='error during running test 021'

  assertCheckPoint(browser, 'TID_021_1', TEST_ERR_MSG)
  cart_page_po = cart_page.Main(browser)
  cart_page_po.tapBottomBarOrderHistoryButton()

  assertCheckPoint(browser, 'TID_021_2', TEST_ERR_MSG)

  json_metadata['TID_021'] = 'passed'
