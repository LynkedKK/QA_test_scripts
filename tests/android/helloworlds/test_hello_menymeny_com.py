
import os,sys

sys.path.append(os.path.dirname(__file__)+'/..')
from lib.config import *

from lib.steps.dismiss_jp_translation import dismiss_jp_translation_in_chrome_browser
from lib.steps.goto_chrome_setting_language_and_disable_auto_translate import gotoChromeSettingLanguageAndDisableAutoTranslate

import unittest
import os
import copy
import sys

from time import sleep

from appium import webdriver

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait


TEST_DIR=os.path.abspath(os.path.dirname(__file__))
REPORT_DIR='/home/logic/_workspace/xxxxxx1/tests/User/reports'
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
    driver.save_screenshot('{}/helloworld_menymeny_com_food.png'.format(SCREENCAPTURE_DIR))

    context = driver.current_context
    driver.switch_to.context("NATIVE_APP")
    sleep(1)
    driver.find_element_by_id("com.android.chrome:id/terms_accept").click()
    sleep(1)

    driver.find_element_by_id("com.android.chrome:id/negative_button").click()
    sleep(1)

    # NOTES: dismiss japanese auto translation
    # dismiss_jp_translation_in_chrome_browser(driver)
    gotoChromeSettingLanguageAndDisableAutoTranslate(driver)

    driver.get('http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/')
    sleep(10)


    driver.switch_to.context("WEBVIEW_chrome")



    driver.save_screenshot('{}/after_helloworld_menymeny_com_food.png'.format(SCREENCAPTURE_DIR))
