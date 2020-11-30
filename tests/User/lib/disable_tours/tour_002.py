
from create_appium_instance import *
from assert_check_point import *
import line_up_page
from urls import *

def tour_002(json_metadata, browser):
  ERR_MSG_BEFORE_TAPPING_TNC_MSG='error found before tapping t n c message'
  ERR_MSG_BACK_FROM_TNC_MSG = 'error found during tapping back from tnc message'

  line_up_page_po = line_up_page.FirstTimeLanding(browser)

  assertCheckPoint(browser, 'TID_002_1', ERR_MSG_BEFORE_TAPPING_TNC_MSG)
  line_up_page_po.tapTAndCText()
  sleep(1)
  assertCheckPoint(browser, 'TID_002_2', ERR_MSG_BACK_FROM_TNC_MSG)

  # back after test
  line_up_page_po.backFromTAndCText()
  assertCheckPoint(browser, 'TID_002_3', ERR_MSG_BACK_FROM_TNC_MSG)

  json_metadata['TID_002'] = 'passed'
  return browser