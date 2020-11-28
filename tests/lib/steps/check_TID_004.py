import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from config import *
from time import sleep
from assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  ERR_MSG_ERR_FOUND_BEFORE_RUNNING_004='error found before running TID_004'
  ERR_MSG_TNC_DIALOGUE_SHOULD_CLOSE='tapping close button , T&C dialog message should close'

  assertCheckPoint(browser, 'TID_004_1', ERR_MSG_ERR_FOUND_BEFORE_RUNNING_004)
  line_up_page_po = line_up_page.FirstTimeLanding(browser)

  line_up_page_po.tapCrossButton()

  assertCheckPoint(browser, 'TID_004_2', ERR_MSG_TNC_DIALOGUE_SHOULD_CLOSE)
  json_metadata['TID_004'] = 'passed'