import random
from pprint import pprint

from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  TEST_ERR_MSG='test failed at TID_026'

  assertCheckPoint(browser, 'TID_026_1', TEST_ERR_MSG)

  json_metadata['TID_026'] = 'passed'
