# http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/?do_lineup

import os,sys
from pprint import pprint
from selenium.webdriver.common.by import By

# todo: refactor me
sys.path.append('/home/logic/_workspace/LYNKED_QA_project/tests/lib/pages')
import item_add_page


ACCEPT_AND_CONTINUE_XPATH='//*[@value="同意して予約する"]'
# ACCEPT_AND_CONTINUE_XPATH='//*[@value="同意して予約する"]'
BACK_BUTTON_XPATH='//*[@id="tac-link"]/div/div'
CROSS_BUTTON_XPATH='//*[@id="close"]'
# LINE_UP_ICON_XPATH='/html/body/main/header/div/div[3]'
BOTTOM_LINE_UP_ICON_XPATH='//*[@id="divLineupInfo"]'
LINE_UP_ICON_XPATH=BOTTOM_LINE_UP_ICON_XPATH

BOTTOM_FOOD_MENU_ICON_XPATH='//*[@id="menu"]'
BOTTOM_CART_ICON_XPATH='//*[@id="cart"]'
BOTTOM_ORDERHISTORY_ICON_XPATH='//*[@id="orderhistory"]'
BOTTOM_STAFF_ICON_XPATH='//*[@id="staff"]'

# TOP_RIGHT_GREEN_BUTTON='//*[@id="userInfo"]'
TOP_RIGHT_GREEN_BUTTON='//*[@id="divLineupInfo"]'

# CART BUTTON IN BOTTOM BAR
CART_BUTTON_XPATH=BOTTOM_CART_ICON_XPATH

HELLOWORLD_FOOD_ITEM1='//*[@id="app"]/div[1]/div[1]/main/div[5]/ul/li[1]/ul/li[1]'
HELLOWORLD_FOOD_ITEM2='//*[@id="app"]/div[1]/div[1]/main/div[5]/ul/li[1]/ul/li[2]'



def helloworld():
  print('helloworld')

def first_time_landing():
  pass

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def getFoodItemFromList(self, food_item_idx):
      # return '/html/body/main/div[6]/ul/li[1]/ul/li[{}]/div/div'.format(food_item_idx)
      return '//*[@id="app"]/div[1]/div[1]/main/div[5]/ul/li[1]/ul/li[{}]'.format(food_item_idx)

    def takeScreenshot(self, sc_filename):
        self.driver.save_screenshot(sc_filename)

    def tapButton(self, xpath):
      ele_button = self.driver.find_element_by_xpath(xpath)
      ele_button.click()

    def tapFoodItemByIdx(self, food_idx):
      food_xpath=self.getFoodItemFromList(food_idx)
      self.tapButton(food_xpath)

    def tapCartButton(self):
      self.tapButton(BOTTOM_CART_ICON_XPATH)

    def getOrderHistoryIcon(self):
      pass

class Main(BasePage):
  def getLineUpIcon(self):
    return self.driver.find_element_by_xpath(LINE_UP_ICON_XPATH)

  def getFoodMenuIcon(self):
    return self.driver.find_element_by_xpath(BOTTOM_FOOD_MENU_ICON_XPATH)

  def tapLineUpIcon(self):
    self.getLineUpIcon().click()

  def tapTopRightGreenButton(self):
    self.tapButton(TOP_RIGHT_GREEN_BUTTON)

  def tapFoodMenuIcon(self):
    self.getFoodMenuIcon().click()

  def tapOrderhistoryIcon(self):
    self.tapButton(BOTTOM_ORDERHISTORY_ICON_XPATH)


  def user_had_placed_few_orders(self, food_item_idx=1, food_item_qty=1):
    self.tapFoodMenuIcon()
    self.tapFoodItemByIdx(food_item_idx)

    item_add_page_po = item_add_page.Main(self.driver)
    for i in range(0,food_item_qty+1):
      item_add_page_po.addFood()

    item_add_page_po.tapAddIntoCartButton()

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
      self.tapButton(CROSS_BUTTON_XPATH)

    # def is_title_matches(self):
    #     """Verifies that the hardcoded text "Python" appears in page title"""
    #     return "Python" in self.driver.title

    # def click_go_button(self):
    #     """Triggers the search"""
    #     element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
    #     element.click()
