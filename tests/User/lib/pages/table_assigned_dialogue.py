# http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/?do_lineup

import os,sys
from pprint import pprint
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


ACCEPT_AND_CONTINUE_XPATH='//*[@value="同意して予約する"]'
# ACCEPT_AND_CONTINUE_XPATH='//*[@value="同意して予約する"]'
BACK_BUTTON_XPATH='//*[@id="tac-link"]/div/div'
CROSS_BUTTON_XPATH='//*[@id="close"]'

NAME_INPUT='/html/body/main/div[8]/div[2]/div/div[1]/input'
NOTE_INPUT='/html/body/main/div[8]/div[2]/div/div[3]/textarea'
AMOUNT_OF_PEOPLE_XPATH='//*[@id="adult"]'
AMOUNT_OF_CHILDREN_XPATH='//*[@id="child"]'

SUBMIT_TICKET_XPATH='/html/body/main/div[8]/div[2]/div/div[4]'

OK_BUTTON_PATH="//div[contains(@class, 'alert')]/input"

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


    def inputAmountOfPeople(self, xpath, number_of_people):
      sys.exit()
      pass

# T&C accepted
class Main(BasePage):
  def inputName(self, customer_name):
    self.inputTextByXpath(NAME_INPUT, customer_name)

  def inputNotes(self, customer_notes):
    self.inputTextByXpath(NOTE_INPUT, customer_notes)

  def tapOkButtonOnDialogue(self):
    sleep(1)
    self.tapButton(OK_BUTTON_PATH)
    # elem = self.driver.find_element_by_xpath(OK_BUTTON_PATH)
    # ac = ActionChains(self.driver)
    # ac.move_to_element(elem).move_by_offset(10, 10).click().perform()
