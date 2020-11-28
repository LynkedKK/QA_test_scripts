# http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/?do_lineup

import os,sys
from pprint import pprint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

NUMBER_OF_PEOPLE_XPATH='//*[@id="app"]/div[1]/div[1]/main/div[3]/div[2]/select'

def po_helloworld():
  print('po_helloworld helloworld')
  assert False, 'po_helloworld launched'
  return 'po_helloworld helloworld'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def tapButton(self, xpath):
      ele_button = self.driver.find_element_by_xpath(xpath)
      ele_button.click()

class Main(BasePage):
  def getLineUpIcon(self):
    return self.driver.find_element_by_xpath(LINE_UP_ICON_XPATH)

  def tapLineUpIcon(self):
    self.getLineUpIcon().click()

  def tapTopRightGreenButton(self):
    self.tapButton(TOP_RIGHT_GREEN_BUTTON)


class WithOrder(Main):
  def updateNumberOfPeople(self, number_of_people_to_select):
    select= Select(self.driver.find_element_by_xpath(NUMBER_OF_PEOPLE_XPATH))
    select.select_by_visible_text(str(number_of_people_to_select)+"人")


class FirstTimeLanding(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    # search_text_element = SearchTextElement()
    def helloworld(self):
      print('helloworld')
