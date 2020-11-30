from lib.asserts.assert_image import assertSameImage
from time import sleep
import base64

import lib.config as config

def takeScreenshot(driver, sc_filename):
  try:
    img_data = driver.get_screenshot_as_base64()
    with open(sc_filename, "wb") as fh:
      fh.write(base64.urlsafe_b64decode(img_data))

  except Exception as e:
    assert False, "takeScreenshot: {}".format(sc_filename)
    # driver.save_screenshot(sc_filename)

def getActualScreenshotPath(test_number):
  return '{}/actual/{}_sc.png'.format(config.SCREENCAPTURE_DIR, test_number)

def getExpectedScreenshotPath(test_number):
  return '{}/expected/{}_sc.png'.format(config.SCREENCAPTURE_DIR, test_number)

def assertCheckPoint(driver ,check_point_name, error_message, fail_threshold=0.05, sleep_s=0.5):
  sleep(sleep_s)
  actual_screenshot_path=getActualScreenshotPath(check_point_name)
  expected_screenshot_path=getExpectedScreenshotPath(check_point_name)

  takeScreenshot(driver, actual_screenshot_path)

  # TODO: RESUME ME
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,fail_threshold,  error_message)
