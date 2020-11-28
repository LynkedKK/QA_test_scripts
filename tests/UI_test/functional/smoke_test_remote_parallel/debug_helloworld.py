import os,sys
from pprint import pprint
from time import sleep

from selenium.webdriver.common.touch_actions import TouchActions

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *
from setupLocalChrome import *

from steps import *
from pages.config import *
from jp import *

def center_of_element(x,y,w,h):
  return (x+w/2, y+h/2)

def test_TID_helloworld(json_metadata):

  browser = setupLocalChrome()
  # browser.get("http://127.0.0.1:46425/test_div_array.html")
  browser.get("https://www.cssscript.com/demo/handle-long-press-tap-event-in-javascript-long-press-js/")

  sleep(5)

  action = TouchActions(browser)
  e = browser.find_element_by_xpath('/html/body/div[2]/div[1]')
  # action.long_press(ele)

  # action.tap_and_hold(finger_x, finger_y).release(finger_x, finger_y).perform()
  action.long_press(e).perform()
  assert False, 'hellofail'

  sleep(10)
  return browser
