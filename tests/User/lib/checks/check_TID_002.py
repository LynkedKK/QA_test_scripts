import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
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