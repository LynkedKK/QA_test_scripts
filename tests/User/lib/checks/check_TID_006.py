import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import *

def run_check(json_metadata, browser, TEST_USER="TID_006_USER", TEST_NOTE='this is some note', num_of_adult=2, num_of_child=3):
  TEST_ERR_MSG='User should automatically direct to food menu page with a number display dialog'

  line_up_po = line_up_page.Main(browser)
  dialogue_po= line_up_confirmation_dialogue.Main(browser)

  line_up_po.inputName(TEST_USER)
  line_up_po.inputNotes(TEST_NOTE)
  line_up_po.changeNumberOfAdult(num_of_adult)
  line_up_po.changeNumberOfChild(num_of_child)

  assertCheckPoint(browser, 'TID_006_1', TEST_ERR_MSG)
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

  line_up_po.submitLineUpTicket()

  dialogue_po.tapOkButtonOnDialogue()
  json_metadata['TID_006'] = 'passed'
