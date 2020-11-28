import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from config import *
from time import sleep
from assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  ERR_MSG='T&C dialog message should close'
  fl_page = food_menu.Main(browser)
  fl_page.tapLineUpIcon()

  assertCheckPoint(browser, 'TID_005_1', ERR_MSG)
  json_metadata['TID_005'] = 'passed'
