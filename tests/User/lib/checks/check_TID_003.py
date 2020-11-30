import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page

from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import *

def run_check(json_metadata, browser):
  ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND='first time landing not found'
  ERR_MSG_ERR_FOUND_TAPPING_ACCEPT_AND_CONTINUE_BUTTON='error found after tapping accept and continue button'

  assertCheckPoint(browser, 'TID_003_1', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND)
  line_up_page_po = line_up_page.FirstTimeLanding(browser)
  line_up_page_po.tapAcceptAndContinueButton()
  sleep(1)

  assertCheckPoint(browser, 'TID_003_2', ERR_MSG_ERR_FOUND_TAPPING_ACCEPT_AND_CONTINUE_BUTTON)
  json_metadata['TID_003'] = 'passed'
