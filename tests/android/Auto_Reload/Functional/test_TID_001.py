import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from lib.asserts.assert_check_point import *
from lib.utils.close_appium_session import *
from lib.steps.create_appium_instance import *
from lib.utils.get_current_test import *

import lib.pages.line_up_page as line_up_page
from lib.urls import *

def tour_TID_001(json_metadata):
  browser=createClientDevice(json_metadata)
  browser.get(LINE_UP_PAGE)

  # dismiss_jp_translation(browser)
  getScreenShot(browser, '{}/dismiss_japan_translation.png'.format(SCREENCAPTURE_DIR))

  line_up_page_po = line_up_page.FirstTimeLanding(browser)
  sleep(0.1)

  line_up_page_po.gotoLineUpPage()
  sleep(0.1)

  assertCheckPoint(browser, 'TID_001_1', 'ERROR_MESSAGE')

  return browser
