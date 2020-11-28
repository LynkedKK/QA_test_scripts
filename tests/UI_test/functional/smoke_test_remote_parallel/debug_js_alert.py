import os,sys
from pprint import pprint
from time import sleep

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
  browser.get("http://127.0.0.1:8003/test_js_alert.html")
  # browser.get("https://www.cssscript.com/demo/handle-long-press-tap-event-in-javascript-long-press-js/")

  sleep(1)

  # action.long_press(ele)

  alert = WebDriverWait(browser, 3).until(expected_conditions.alert_is_present())
  text = alert.text

  # action.tap_and_hold(finger_x, finger_y).release(finger_x, finger_y).perform()
  # action.long_press(e).perform()

  alert.accept()

  assert False, text

  sleep(10)
  return browser
