import unittest
import os
import copy
import sys

import base64

from time import sleep

from appium import webdriver

from lib.steps.goto_chrome_setting_language_and_disable_auto_translate import gotoChromeSettingLanguageAndDisableAutoTranslate

from lib.steps.goto_chrome_setting_language_and_disable_auto_translate import DEVICE_MOBILE, DEVICE_TABLET

SCREENCAPTURE_DIR='/home/logic/_workspace/LYNKED_QA_project/tests/User/reports/assets'

def getScreenShot(driver, sc_filename):
  img_data = driver.get_screenshot_as_base64()
  with open(sc_filename, "wb") as fh:
    fh.write(base64.urlsafe_b64decode(img_data))


def createClientDevice(json_metadata):
  driver = connectToAppium(json_metadata)
  gotoChromeSettingLanguageAndDisableAutoTranslate(driver, DEVICE_MOBILE)

  driver.get('http://www.example.com')
  sleep(15)
  driver.switch_to.context("WEBVIEW_chrome")

  return create_appium_instance(json_metadata, driver)

def getContexts(json_metadata, driver):
  return driver.contexts

def wantedContextAvailable(json_metadata, driver, wanted_context):
  # true if available
  return wanted_context in getContexts(json_metadata, driver)


def createRestaurantDevice(json_metadata):
  driver = connectToAppium(json_metadata, 5723, 9201, 8201, 8001)
  gotoChromeSettingLanguageAndDisableAutoTranslate(driver, DEVICE_TABLET)

  driver.get('http://www.example.com')
  sleep(1)

  while not(wantedContextAvailable(json_metadata, driver, 'WEBVIEW_chrome')):
    sleep(0.2)

  sleep(1)
  driver.switch_to.context("WEBVIEW_chrome")

  return create_appium_instance(json_metadata, driver, 5723)

def connectToAppium(json_metadata,appium_port=4723, mjpegServerPort=9200, systemPort=8200, chromedriverPort=8000):
  desired_caps = {
      "platformName": "Android",
      "appPackage": "com.android.chrome",
      "appActivity": "com.google.android.apps.chrome.Main",
      "automationName": "UiAutomator2",
      "clearSystemFiles":True,
      "disableWindowAnimation":True,
      "newCommandTimeout": 120,
      "mjpegServerPort": mjpegServerPort,
      "systemPort": systemPort,
      "fastReset": True,
      "printPageSourceOnFindFailure":True,
      "clearSystemFiles":True
  }

  driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(appium_port), desired_caps)
  driver.implicitly_wait(10)
  getScreenShot(driver, '{}/example_com_screen.png'.format(SCREENCAPTURE_DIR))

  context = driver.current_context
  driver.switch_to.context("NATIVE_APP")
  sleep(1)
  driver.find_element_by_id("com.android.chrome:id/terms_accept").click()
  sleep(1)

  driver.find_element_by_id("com.android.chrome:id/negative_button").click()
  sleep(1)



  return driver


def create_appium_instance(json_metadata, driver, appium_port=4723):
  getScreenShot(driver, '{}/after_example_com_screen.png'.format(SCREENCAPTURE_DIR))

  ele_h1 = driver.find_element_by_xpath('/html/body/div/h1')
  sleep(1)

  # NOTES: simple health check
  assert 'Example Domain'==ele_h1.text

  return driver