
from lib.utils.get_current_test import *
from time import sleep

def close_appium_session(browser, calling_func_name):
  # called by the test itself, quit appium
  if (calling_func_name == get_current_test()):
    browser.quit()

    # cool down emulator
    sleep(5)

  # called not by the test itself, kee
  return browser