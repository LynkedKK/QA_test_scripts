import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from config import *
from time import sleep
from assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  ERROR_MESSAGE='The device should auto redirect to line up page'

  # URL = 'http://192.168.88.105:8002/'
  # browser.get(URL)
  browser.get(LINE_UP_PAGE)
  line_up_page_po = line_up_page.FirstTimeLanding(browser)
  sleep(0.1)

  line_up_page_po.gotoLineUpPage()
  sleep(0.1)

  assertCheckPoint(browser, 'TID_001_1', ERROR_MESSAGE)

  json_metadata['TID_001'] = 'passed'