import os,sys
from pprint import pprint
from time import sleep

FIRST_ADD_BUTTON='//*[@id="plus"]'
# add button 1
# /html/body/main/div[8]/div[2]/div[2]/div[2]/div[3]/button[2]

# add button 2
# /html/body/main/div[8]/div[2]/div[3]/div[2]/div[3]/button[2]

# del button 1
# /html/body/main/div[8]/div[2]/div[2]/div[2]/div[3]/button[1]

# remove 削除
# /html/body/main/div[8]/div[2]/div[2]/div[3]/button
# /html/body/main/div[8]/div[2]/div[3]/div[3]/button
# //*[@id="app"]/div[1]/div[1]/main/div[3]/div/div[1]/div[2]/div[2]
# //*[@id="app"]/div[1]/div[1]/main/div[3]/div/div[2]/div[2]/div[2]

TOP_LEFT_CLOSE_BUTTON_XPATH='//*[@id="close"]'

PLACE_ORDER_BUTTON_XPATH='//*[@id="app"]/div[1]/div[1]/main/div[4]/div'

BOTTOM_FOOD_MENU_ICON_XPATH='//*[@id="menu"]'
BOTTOM_CART_ICON_XPATH='//*[@id="cart"]'
BOTTOM_ORDERHISTORY_ICON_XPATH='//*[@id="orderhistory"]'
BOTTOM_STAFF_ICON_XPATH='//*[@id="staff"]'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
      self.driver = driver

    def takeScreenshot(self, sc_filename):
      self.driver.save_screenshot(sc_filename)

    def tapButton(self, xpath):
      ele_button = self.driver.find_element_by_xpath(xpath)
      ele_button.click()

    # TODO: to obsolete
    def getFoodItemXpathFromIdx(self, item_idx):
      return '/html/body/main/div[8]/div[2]/div[{}]'.format(item_idx+1)

    def getAddButtonXpath(self, item_idx):
      return '/html/body/div/div[1]/div[1]/main/div[3]/div/div[{}]/div[2]/div[1]/button[1]'.format(item_idx)

    def getMinusButtonXpath(self, item_idx):
      return '/html/body/div/div[1]/div[1]/main/div[3]/div/div[{}]/div[2]/div[1]/button[2]'.format(item_idx)

    def getRemoveButtonXpath(self, idx):
      return '//*[@id="app"]/div[1]/div[1]/main/div[3]/div/div[{}]/div[2]/div[2]'.format(idx)

    def tapAddButton(self, item_idx, sleep_after_tap_s=0.1):
      self.tapButton(self.getAddButtonXpath(item_idx))
      sleep(sleep_after_tap_s)

    def tapMinusButton(self, item_idx, sleep_after_tap_s=0.1):
      self.tapButton(self.getMinusButtonXpath(item_idx))
      sleep(sleep_after_tap_s)

    def tapRemoveButton(self, item_idx):
      self.tapButton((self.getRemoveButtonXpath(item_idx)))

    def tapTopLeftCloseButton(self):
      self.tapButton(TOP_LEFT_CLOSE_BUTTON_XPATH)

    def tapPlaceOrderButton(self):
      self.tapButton(PLACE_ORDER_BUTTON_XPATH)

    def tapOrderhistoryIcon(self):
      self.tapButton(BOTTOM_ORDERHISTORY_ICON_XPATH)

class Main(BasePage):
  def getLineUpIcon(self):
    return self.driver.find_element_by_xpath(LINE_UP_ICON_XPATH)

  def tapLineUpIcon(self):
    self.getLineUpIcon().click()

  def tapTopRightGreenButton(self):
    self.tapButton(TOP_RIGHT_GREEN_BUTTON)

  def tapBottomBarMenuButton(self):
    self.tapButton('//*[@id="menu"]')

  def tapBottomBarCartButton(self):
    self.tapButton('//*[@id="cart"]')

  def tapBottomBarOrderHistoryButton(self):
    self.tapButton(BOTTOM_ORDERHISTORY_ICON_XPATH)

class FirstTimeLanding(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    # search_text_element = SearchTextElement()
    def helloworld(self):
      print('helloworld')
