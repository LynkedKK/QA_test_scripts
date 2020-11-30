import unittest
import os
import copy
import sys

from time import sleep

from appium import webdriver

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait


TEST_DIR=os.path.abspath(os.path.dirname(__file__))
REPORT_DIR='/home/logic/_workspace/xxxxxxx/tests/User/reports'
SCREENCAPTURE_DIR=os.path.abspath('{}/assets'.format(REPORT_DIR))

class AndroidMobileWebTest(unittest.TestCase):
  def test_should_create_and_destroy_android_web_session(self):
    desired_caps = {
        "platformName": "Android",
        "appPackage": "com.android.chrome",
        "appActivity": "com.google.android.apps.chrome.Main"
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    sleep(3)
    driver.save_screenshot('{}/chrome_welcome_screen.png'.format(SCREENCAPTURE_DIR))

    context = driver.current_context
    driver.switch_to.context("NATIVE_APP")
    sleep(1)
    driver.find_element_by_id("com.android.chrome:id/terms_accept").click()
    sleep(1)

    driver.find_element_by_id("com.android.chrome:id/negative_button").click()
    sleep(1)


    driver.get('http://www.example.com')
    sleep(10)

    driver.switch_to.context("WEBVIEW_chrome")

    driver.save_screenshot('{}/after_chrome_welcome_screen.png'.format(SCREENCAPTURE_DIR))

    ele_h1 = driver.find_element_by_xpath('/html/body/div/h1')
    sleep(1)

    assert 'Example Domain'==ele_h1.text
