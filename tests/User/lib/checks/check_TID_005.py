import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import *

def run_check(json_metadata, browser):
  ERR_MSG='T&C dialog message should close'
  fl_page = food_menu.Main(browser)
  fl_page.tapLineUpIcon()

  assertCheckPoint(browser, 'TID_005_1', ERR_MSG)
  json_metadata['TID_005'] = 'passed'
