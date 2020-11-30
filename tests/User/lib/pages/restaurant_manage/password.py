import os,sys
from pprint import pprint

PASSWORD_INPUT_XPATH='//*[@id="root"]/main/div/div[1]/div[2]/input'
LOGIN_BUTTON_XPATH='//*[@id="root"]/main/div/div[3]/div'

def po_helloworld():
  print('po_helloworld helloworld')
  assert False, 'po_helloworld launched'
  return 'po_helloworld helloworld'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def takeScreenshot(self, sc_filename):
        self.driver.save_screenshot(sc_filename)

    def tapButton(self, xpath):
      ele_button = self.driver.find_element_by_xpath(xpath)
      ele_button.click()

    def inputTextByXpath(self, xpath, text_to_input):
      ele_button = self.driver.find_element_by_xpath(xpath)
      ele_button.send_keys(text_to_input)

class Main(BasePage):
  def getLineUpIcon(self):
    return self.driver.find_element_by_xpath(LINE_UP_ICON_XPATH)

  def tapLineUpIcon(self):
    self.getLineUpIcon().click()

  def tapTopRightGreenButton(self):
    self.tapButton(TOP_RIGHT_GREEN_BUTTON)

  def inputPassword(self, password_to_input):
    self.inputTextByXpath(PASSWORD_INPUT_XPATH, password_to_input)

  def tapLogin(self):
    self.tapButton(LOGIN_BUTTON_XPATH)

class FirstTimeLanding(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    # search_text_element = SearchTextElement()
    def helloworld(self):
      print('helloworld')
