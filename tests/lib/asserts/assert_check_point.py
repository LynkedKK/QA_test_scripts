import os,sys

from time import sleep
from random import randrange

from assert_image import assertSameImage

def takeScreenshot(driver, sc_filename):
    driver.save_screenshot(sc_filename)

def getRandomString():
  return randrange(1,100)

def getActualScreenshotPath(test_number):
  random_string = getRandomString()
  # return 'tests/UI_test/functional/smoke_test_remote_parallel/actual/{}_sc.png'.format(test_number)
  return 'tests/UI_test/functional/smoke_test_remote_parallel/actual/{}_sc_{}.png'.format(test_number, random_string)

def getExpectedScreenshotPath(test_number):
  return 'tests/UI_test/functional/smoke_test_remote_parallel/expected/{}_sc.png'.format(test_number)

def assertCheckPoint(driver ,check_point_name, error_message, fail_threshold=0.054, sleep_s=0.5, make_asserts=True):
  sleep(sleep_s)
  actual_screenshot_path=getActualScreenshotPath(check_point_name)
  expected_screenshot_path=getExpectedScreenshotPath(check_point_name)

  takeScreenshot(driver, actual_screenshot_path)

  if make_asserts:
    assertSameImage(expected_screenshot_path, actual_screenshot_path,fail_threshold,  error_message)

  # os.remove(actual_screenshot_path)
