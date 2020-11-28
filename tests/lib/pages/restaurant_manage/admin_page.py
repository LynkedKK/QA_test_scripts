import os,sys
from pprint import pprint

PASSWORD_INPUT_XPATH='//*[@id="root"]/main/div/div[1]/div[2]/input'
LOGIN_BUTTON_XPATH='//*[@id="root"]/main/div/div[3]/div'
SITE_NAVIGATOR_BUTTON_XPATH='//*[@id="root"]/header/div[1]/div[1]/button'


BACK_BUTTON_XPATH='//*[@id="admin_sidebar"]/div[1]'
SEAT_RESERVATION_MANAGMENT_BUTTON_XPATH='//*[@id="admin_sidebar"]/div[2]'
ORDER_MANAGMENT_BUTTON_XPATH='//*[@id="admin_sidebar"]/div[3]'
ACCOUNT_MANAGMENT_BUTTON_XPATH='//*[@id="admin_sidebar"]/div[4]'
RESTAURANT_MENU_MANAGMENT_BUTTON_XPATH='//*[@id="admin_sidebar"]/div[5]'


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

  def tapSiteNavigator(self):
    self.tapButton(SITE_NAVIGATOR_BUTTON_XPATH)

  # click at any unassigned user table
  def tapUnassignedUserTable(self, idx=1):
    self.tapButton('//*[@id="divLineupGuestList"]/div[{}]'.format(idx))

  # Assign the user to any table number
  def assignTable(self, table_number=1):
    self.inputTextByXpath('//*[@id="seat_number"]',str(table_number))

  # Assign the user to any table number
  def assignTableSubmit(self):
    self.tapButton('//*[@id="seat_management"]/input[2]')

class FirstTimeLanding(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    # search_text_element = SearchTextElement()
    def helloworld(self):
      print('helloworld')


class SiteNavigatorPopup(Main):


    #Declares a variable that will contain the retrieved text
    # search_text_element = SearchTextElement()
    def helloworld(self):
      print('helloworld')

    def tapBackButton(self):
      self.tapButton(BACK_BUTTON_XPATH)

    # line up button, lineup button
    def tapSeatReservationManagmentButton(self):
      self.tapButton(SEAT_RESERVATION_MANAGMENT_BUTTON_XPATH)

    # food control
    def tapOrderManagmentButton(self):
      self.tapButton(ORDER_MANAGMENT_BUTTON_XPATH)

    def tapAccountManagmentButton(self):
      self.tapButton(ACCOUNT_MANAGMENT_BUTTON_XPATH)

    def tapRestaurantMenuManagmentButton(self):
      self.tapButton(RESTAURANT_MENU_MANAGMENT_BUTTON_XPATH)
