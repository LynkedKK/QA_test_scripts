
import os,sys
from pprint import pprint

ACCEPT_AND_CONTINUE_XPATH='//*[@value="同意して予約する"]'

# ADD_BUTTON_XPATH='/html/body/main/div[8]/div[2]/div[5]/div[1]/button[2]'
# DEL_BUTTON_XPATH='/html/body/main/div[8]/div[2]/div[5]/div[1]/button[1]'

ADD_BUTTON_XPATH='//*[@id="app"]/div[1]/div[1]/main/div[6]/div[2]/div[5]/button[1]'
DEL_BUTTON_XPATH='//*[@id="app"]/div[1]/div[1]/main/div[6]/div[2]/div[5]/button[2]'

NUM_OF_ITEM_XPATH='/html/body/main/div[8]/div[2]/div[5]/div[1]/div'
UNIT_PRICE_XPATH='/html/body/main/div[8]/div[2]/div[4]/div'
FOOD_NAME_XPATH='/html/body/main/div[8]/div[2]/div[2]/div'
FOOD_INFO_XPATH='/html/body/main/div[8]/div[2]/div[3]/div'

TOP_LEFT_CLOSE_BUTTON_XPATH='//*[@id="close"]'
ADD_INTO_CART_BUTTON_XPATH='//*[@id="addtocart"]'

CROSS_BUTTON_XPATH='//*[@id="close"]'
BOTTOM_CART_PAGE_BUTTON_XPATH='//*[@id="cart"]'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
      self.driver = driver

    def tapButton(self, xpath):
      ele_button = self.driver.find_element_by_xpath(xpath)
      ele_button.click()

    def addFood(self):
      self.tapButton(ADD_BUTTON_XPATH)

    def removeFood(self):
      self.tapButton(DEL_BUTTON_XPATH)

    def takeScreenshot(self, sc_filename):
        self.driver.save_screenshot(sc_filename)

    def tapAddIntoCartButton(self):
      self.tapButton(ADD_INTO_CART_BUTTON_XPATH)

class Main(BasePage):
  def getLineUpIcon(self):
    return self.driver.find_element_by_xpath(LINE_UP_ICON_XPATH)

  def tapLineUpIcon(self):
    self.getLineUpIcon().click()

  def tapTopRightGreenButton(self):
    self.tapButton(TOP_RIGHT_GREEN_BUTTON)

  def tapCrossButton(self):
    print('redirect me using tapTopLeftCloseButton')
    self.tapButton(CROSS_BUTTON_XPATH)

  def tapBottomCartPageButton(self):
    self.tapButton(BOTTOM_CART_PAGE_BUTTON_XPATH)


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


    # def is_title_matches(self):
    #     """Verifies that the hardcoded text "Python" appears in page title"""
    #     return "Python" in self.driver.title

    # def click_go_button(self):
    #     """Triggers the search"""
    #     element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
    #     element.click()
