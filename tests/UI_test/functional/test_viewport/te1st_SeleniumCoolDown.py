import os,sys
from pprint import pprint
from time import sleep

from selenium import webdriver

from viewports import *
# from tests.UI_test.functional.test_viewport.config import SCREENCAPTURE_PATH
from config import *

SELENIUM_HUB_HOST='localhost'

def test_SeleniumCoolDown():
  selenium_url = 'http://{}:4444/wd/hub'.format(SELENIUM_HUB_HOST)

  browser = webdriver.Remote(
    command_executor=selenium_url,
    desired_capabilities = {
      "browserName":"firefox",
      "version":"",
      "platform":"LINUX"
      })

  browser.get('http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/')

  browser.quit()
  sleep(30)


  browser = webdriver.Remote(
    command_executor=selenium_url,
    desired_capabilities = {
      "browserName":"firefox",
      "version":"",
      "platform":"LINUX"
      })

  browser.get('http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/')

  browser.quit()
  sleep(30)