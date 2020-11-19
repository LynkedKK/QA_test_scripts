import os,sys
from pprint import pprint

ACCEPT_AND_CONTINUE_XPATH='//*[@id="tac-container"]/div[2]/div[5]/input'

def helloworld():
  print('helloworld')

def first_time_landing():
  pass

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class CheckPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    # search_text_element = SearchTextElement()
    def helloworld(self):
      print('helloworld')

    def checkLinkExist(self):
      self.find_element_by_id('test_link')

    def checkAcceptAndContinueButtonExist(self):
      self.find_element_by_xpath(ACCEPT_AND_CONTINUE_XPATH)

    # def is_title_matches(self):
    #     """Verifies that the hardcoded text "Python" appears in page title"""
    #     return "Python" in self.driver.title

    # def click_go_button(self):
    #     """Triggers the search"""
    #     element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
    #     element.click()
