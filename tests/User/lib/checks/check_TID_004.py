import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import *

def run_check(json_metadata, browser):
  ERR_MSG_ERR_FOUND_BEFORE_RUNNING_004='error found before running TID_004'
  ERR_MSG_TNC_DIALOGUE_SHOULD_CLOSE='tapping close button , T&C dialog message should close'

  assertCheckPoint(browser, 'TID_004_1', ERR_MSG_ERR_FOUND_BEFORE_RUNNING_004)
  line_up_page_po = line_up_page.FirstTimeLanding(browser)

  line_up_page_po.tapCrossButton()

  assertCheckPoint(browser, 'TID_004_2', ERR_MSG_TNC_DIALOGUE_SHOULD_CLOSE)
  json_metadata['TID_004'] = 'passed'
