
from create_appium_instance import *
from assert_check_point import *
import line_up_page
from urls import *

def tour_003(json_metadata, browser):
  ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND='first time landing not found'
  ERR_MSG_ERR_FOUND_TAPPING_ACCEPT_AND_CONTINUE_BUTTON='error found after tapping accept and continue button'

  assertCheckPoint(browser, 'TID_003_1', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND)
  line_up_page_po = line_up_page.FirstTimeLanding(browser)
  line_up_page_po.tapAcceptAndContinueButton()
  sleep(1)

  assertCheckPoint(browser, 'TID_003_2', ERR_MSG_ERR_FOUND_TAPPING_ACCEPT_AND_CONTINUE_BUTTON)
  json_metadata['TID_003'] = 'passed'