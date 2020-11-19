import os,sys
from pprint import pprint
from selenium.webdriver.common.by import By


ACCEPT_AND_CONTINUE_XPATH='//*[@value="同意して予約する"]'

def helloworld():
  print('helloworld')

def first_time_landing():
  pass

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def takeScreenshot(self, sc_filename):
        self.driver.save_screenshot(sc_filename)

class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    # search_text_element = SearchTextElement()
    def helloworld(self):
      print('helloworld')

    def checkLinkExist(self):
      self.driver.find_element_by_id('test_link')
      self.driver.find_element_by_xpath('//*[@id="test_link"]')

    def checkAcceptAndContinueButtonExist(self):
      ELE_ACCEPT_BUTTON = self.driver.find_element_by_xpath(ACCEPT_AND_CONTINUE_XPATH)
      ELE_ACCEPT_BUTTON.click()
      # self.find_element(By.XPATH, ACCEPT_AND_CONTINUE_XPATH)

      # self.find_element_by_xpath(ACCEPT_AND_CONTINUE_XPATH)

    # def is_title_matches(self):
    #     """Verifies that the hardcoded text "Python" appears in page title"""
    #     return "Python" in self.driver.title

    # def click_go_button(self):
    #     """Triggers the search"""
    #     element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
    #     element.click()
