import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from config import *
from time import sleep
from assert_check_point import assertCheckPoint

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