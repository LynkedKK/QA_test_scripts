import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *


from lib.urls import *
from lib.steps.create_appium_instance import *

# from Auto_Reload.Functional.test_TID_006_1 import tour_TID_006_1 as tour_TID_006_1
import lib.checks.check_TID_026 as check_TID_026

# from setupLocalChrome import *
def tour_TID_026(json_metadata):
  r_browser=createRestaurantDevice(json_metadata)

  r_browser.start_recording_screen()

  # restaurant_manage_browser = setupLocalChrome()
  r_browser.get(RESTURANT_MANAGE_URL)
  # pre condition
  # get to lineup page
  check_TID_026.run_check(json_metadata, r_browser)


  return r_browser

  # assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,0.1,  'first time landing test after clicking accept failed')