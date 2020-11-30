
import os,sys
from pprint import pprint
from time import sleep

OK_BUTTON_PATH='//*[@id="alert"]/div[2]/input'

def po_helloworld():
  print('po_helloworld helloworld')
  return 'po_helloworld helloworld'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def tapButton(self, xpath):
      ele_button = self.driver.find_element_by_xpath(xpath)
      ele_button.click()

    def takeScreenshot(self, sc_filename):
      self.driver.save_screenshot(sc_filename)

class Main(BasePage):
  # def getLineUpIcon(self):
  #   return self.driver.find_element_by_xpath(LINE_UP_ICON_XPATH)

  def tapOkButtonOnDialogue(self):
    sleep(1)
    self.tapButton(OK_BUTTON_PATH)
    # elem = self.driver.find_element_by_xpath(OK_BUTTON_PATH)
    # ac = ActionChains(self.driver)
    # ac.move_to_element(elem).move_by_offset(10, 10).click().perform()
