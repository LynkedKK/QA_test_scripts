# http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/?do_lineup

import os,sys
from pprint import pprint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

ACCEPT_AND_CONTINUE_XPATH='//*[@value="同意して予約する"]'
# ACCEPT_AND_CONTINUE_XPATH='//*[@value="同意して予約する"]'
BACK_BUTTON_XPATH='//*[@id="tac-link"]/div/div'
# CROSS_BUTTON_XPATH='//*[@id="close"]'

TOP_LEFT_CLOSE_BUTTON='//*[@id="close"]'
CROSS_BUTTON_XPATH=TOP_LEFT_CLOSE_BUTTON

NAME_INPUT='//*[@id="app"]/div[1]/div[1]/main/div[6]/div[2]/div/div[1]/input'
NOTE_INPUT='//*[@id="app"]/div[1]/div[1]/main/div[6]/div[2]/div/div[3]/textarea'
AMOUNT_OF_PEOPLE_XPATH='//*[@id="adult"]'
AMOUNT_OF_CHILDREN_XPATH='//*[@id="child"]'

SUBMIT_TICKET_XPATH='//*[@id="app"]/div[1]/div[1]/main/div[6]/div[2]/div/div[4]/div'
UPDATE_TICKET_INFO_XPATH='//*[@id="app"]/div[1]/div[1]/main/div[6]/div[2]/div/div[4]/div'

ADULT_SELECTOR_XPATH='//*[@id="adult"]'
CHILD_SELECTOR_XPATH='//*[@id="child"]'

def helloworld():
  print('helloworld')

def first_time_landing():
  pass

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def gotoLineUpPage(self):
        self.driver.get('http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/?do_lineup')

    def takeScreenshot(self, sc_filename):
        self.driver.save_screenshot(sc_filename)

    def tapButton(self, xpath):
      ele_button = self.driver.find_element_by_xpath(xpath)
      ele_button.click()

    def inputTextByXpath(self, xpath, text_to_input):
      ele_button = self.driver.find_element_by_xpath(xpath)
      ele_button.send_keys(text_to_input)

    def eleByXpath(self, xpath):
      return self.driver.find_element_by_xpath(xpath)

    def submitLineUpTicket(self):
      self.tapButton(SUBMIT_TICKET_XPATH)


    def updateLineUpTicket(self):
      self.tapButton(UPDATE_TICKET_INFO_XPATH)

    def inputAmountOfPeople(self, xpath, number_of_people):
      sys.exit()
      pass

    def tapTopLeftCloseButton(self):
      self.tapButton(TOP_LEFT_CLOSE_BUTTON)

# T&C accepted
class Main(BasePage):
  def inputName(self, customer_name):
    self.inputTextByXpath(NAME_INPUT, customer_name)

  def inputNotes(self, customer_notes):
    self.inputTextByXpath(NOTE_INPUT, customer_notes)

  def changeNumberOfAdult(self, number_of_adult):
    select= Select(self.driver.find_element_by_xpath(ADULT_SELECTOR_XPATH))
    select.select_by_visible_text(str(number_of_adult)+"人")

  def changeNumberOfChild(self, number_of_child):
    select= Select(self.driver.find_element_by_xpath(CHILD_SELECTOR_XPATH))
    select.select_by_visible_text(str(number_of_child)+"人")

class FirstTimeLanding(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    # search_text_element = SearchTextElement()
    def helloworld(self):
      print('helloworld')

    def checkLinkExist(self):
      self.driver.find_element_by_id('test_link')
      self.driver.find_element_by_xpath('//*[@id="test_link"]')

    def checkAcceptAndContinueButtonExist(self):
      # TODO: return for non exist
      ELE_ACCEPT_BUTTON = self.driver.find_element_by_xpath(ACCEPT_AND_CONTINUE_XPATH)

      # self.find_element(By.XPATH, ACCEPT_AND_CONTINUE_XPATH)

      # self.find_element_by_xpath(ACCEPT_AND_CONTINUE_XPATH)

    def tapTAndCText(self):
      t_and_c_link = self.driver.find_element_by_xpath('//*[@id="tac-container"]/div[2]/div[4]/a')
      t_and_c_link.click()

    def backFromTAndCText(self):
      ele_back_button=self.driver.find_element_by_xpath(BACK_BUTTON_XPATH)
      ele_back_button.click()

    def tapAcceptAndContinueButton(self):
      ELE_ACCEPT_BUTTON = self.driver.find_element_by_xpath(ACCEPT_AND_CONTINUE_XPATH)
      ELE_ACCEPT_BUTTON.click()

    def tapCrossButton(self):
      print('redirect me using tapTopLeftCloseButton')
      self.tapButton(CROSS_BUTTON_XPATH)


    # def is_title_matches(self):
    #     """Verifies that the hardcoded text "Python" appears in page title"""
    #     return "Python" in self.driver.title

    # def click_go_button(self):
    #     """Triggers the search"""
    #     element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
    #     element.click()
