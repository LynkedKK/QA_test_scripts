import os,sys
from pprint import pprint
from time import sleep

from selenium import webdriver

from viewports import *
# from tests.UI_test.functional.test_viewport.config import SCREENCAPTURE_PATH
from config import *

SELENIUM_HUB_HOST='localhost'

def get_sc_filename(SCREENCAPTURE_PATH, viewport_name):
  return '{}/{}_test.png'.format(SCREENCAPTURE_PATH,viewport_name.replace('/','_').replace(' ','_'))

def test_ViewPort_food():
  pprint(get_sc_filename(FOOD_SCREENCAPTURE_PATH,'viewport_name'))
  # sys.exit()

  selenium_url = 'http://{}:4444/wd/hub'.format(SELENIUM_HUB_HOST)

  browser = webdriver.Remote(
    command_executor=selenium_url,
    desired_capabilities = {
      "browserName":"firefox",
      "version":"",
      "platform":"LINUX"
      })

  browser.get('http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/')

  for viewport_config in ALL_VIEWPORTS:
    (viewport_name, dump1, dump2 , width, height) = viewport_config
    sc_filename =get_sc_filename(FOOD_SCREENCAPTURE_PATH,viewport_name)

    browser.set_window_size(width, height)
    browser.save_screenshot(sc_filename)

    # assert('Google'==browser.title)

  browser.quit()
  sleep(30)