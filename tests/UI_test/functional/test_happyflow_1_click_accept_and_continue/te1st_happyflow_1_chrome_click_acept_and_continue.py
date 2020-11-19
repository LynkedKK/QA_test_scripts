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
import first_time_landing

from jp import *

SELENIUM_HUB_HOST='localhost'
FOOD_PAGE='http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/'


def test_happyflow_1_chrome_click_acept_and_continue():
  selenium_url = 'http://{}:4444/wd/hub'.format(SELENIUM_HUB_HOST)

  chrome_options = webdriver.ChromeOptions()
  mobile_emulation = { "deviceName": "Nexus 5" }
  chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

  browser = webdriver.Remote(
    command_executor=selenium_url,
    desired_capabilities = chrome_options.to_capabilities()
  )

  # browser.get(FOOD_PAGE)
  URL = 'http://192.168.88.105:8002/'
  browser.get(FOOD_PAGE)
  sleep(1)

  fl_page = first_time_landing.CheckPage(browser)
  fl_page.checkAcceptAndContinueButtonExist()

  browser.quit()
  sleep(30)
