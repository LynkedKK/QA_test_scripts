
from create_appium_instance import *
from assert_check_point import *
import line_up_page
from urls import *

def tour_001(json_metadata):
  browser=create_appium_instance(json_metadata)
  browser.get(LINE_UP_PAGE)

  line_up_page_po = line_up_page.FirstTimeLanding(browser)
  sleep(0.1)

  line_up_page_po.gotoLineUpPage()
  sleep(0.1)

  assertCheckPoint(browser, 'TID_001_1', 'ERROR_MESSAGE')

  return browser
