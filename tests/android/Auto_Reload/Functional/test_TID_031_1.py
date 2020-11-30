import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_031 import tour_TID_031 as tour_TID_031
import lib.checks.check_TID_031_a as check_TID_031_a

def test_TID_031_1(json_metadata):

  r_browser = tour_TID_031(json_metadata)

  check_TID_031_a.run_check(json_metadata, r_browser)


  # browser.execute_script("mobile:shell", 	{'command': 'echo', 'args': ['arg1', 'arg2']})
  r_browser.terminate_app('com.android.chrome')
  r_browser.reset()
  r_browser.close_app()
  r_browser.quit()


  return r_browser

  # assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,0.1,  'first time landing test after clicking accept failed')