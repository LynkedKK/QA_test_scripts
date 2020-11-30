
from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  TEST_ERR_MSG='It should send order successfully'


  # item_add_page_po=item_add_page.Main(browser)

  # check if red dialogue appears
  assertCheckPoint(browser, 'TID_019_1', TEST_ERR_MSG)

  # cart_page_po.tapPlaceOrderButton()
  # tap ok to dismiss dialogue




  json_metadata['TID_019'] = 'passed'