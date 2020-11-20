import os,sys
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep

TEST_DIR=os.path.dirname(__file__)
FUNCTIONAL_DIR=os.path.abspath(TEST_DIR+'/..')
UI_TEST_DIR=os.path.abspath(FUNCTIONAL_DIR+'/..')
TEST_ROOT=os.path.abspath(UI_TEST_DIR+'/..')
LIB_DIR=os.path.abspath(TEST_ROOT+'/lib')
LIB_PO_DIR=os.path.abspath(LIB_DIR+'/pages')
LIB_ELE_DIR=os.path.abspath(LIB_DIR+'./elements')
LANG_DIR=os.path.abspath(TEST_ROOT+'/lang')
LIB_CONFIG_DIR=os.path.abspath(LIB_DIR+'/configs')
LIB_ASSERT_DIR=os.path.abspath(LIB_DIR+'/asserts')

sys.path.append(LIB_DIR)
sys.path.append(LIB_PO_DIR)
sys.path.append(LANG_DIR)
sys.path.append(LIB_CONFIG_DIR)
sys.path.append(LIB_ASSERT_DIR)

from lib_helloworld import lib_helloworld
from po_helloworld import po_helloworld
from assert_image import assertSameImage
from jp import *

SELENIUM_HUB_HOST='localhost'
FOOD_PAGE='http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/'

ACTUAL_SCREENSHOT='reports/UI_test/functional/test_happyflow_1/result/test_happyflow_1_chrome_first_time_landing_iphonex.png'
EXPECTED_SCREENSHOT='tests/UI_test/functional/test_happyflow_1/expected_result/test_happyflow_1_chrome_first_time_landing_iphonex.png'
IMAGE_TEST_THRESHOLD=0.05

width=375
height=812

def test_happyflow_1_chrome(json_metadata):
  json_metadata['TEST_ID'] = 'TID_001'

  selenium_url = 'http://{}:4444/wd/hub'.format(SELENIUM_HUB_HOST)

  chrome_options = webdriver.ChromeOptions()
  mobile_emulation = { "deviceName": "Nexus 5" }
  chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

  # browser = webdriver.Remote(
  #   command_executor=selenium_url,
  #   desired_capabilities = {
  #     "browserName":"chrome",
  #     "version":"",
  #     # "platform":"LINUX"
  #     },
  #   desired_capabilities = chrome_options.to_capabilities()
  #   )
  # https://chromedriver.chromium.org/mobile-emulation


  browser = webdriver.Remote(
    command_executor=selenium_url,
    desired_capabilities = chrome_options.to_capabilities()
  )

  browser.get(FOOD_PAGE)
  # browser.set_window_size(width, height)
  sleep(1)

  browser.save_screenshot(ACTUAL_SCREENSHOT)

  browser.quit()
  sleep(30)

  assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,IMAGE_TEST_THRESHOLD,  'first time landing test on chrome failed')
