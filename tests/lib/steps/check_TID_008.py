import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from config import *
from time import sleep
from assert_check_point import assertCheckPoint

def run_check(json_metadata, browser, user_name='TID_008_USERNAME', user_note='this is customer notes by louis from script updated'):
  TEST_ERR_MSG='The user info should be updated'

  # before
  fl_page = food_menu.Main(browser)
  line_up_po = line_up_page.Main(browser)
  dialogue_po= line_up_confirmation_dialogue.Main(browser)

  assertCheckPoint(browser, 'TID_008_1', TEST_ERR_MSG)


  # On food menu page, click the number at top right screen

  # Update the name, people, note
  # Update my info
  fl_page.tapTopRightGreenButton()
  assertCheckPoint(browser, 'TID_008_2', TEST_ERR_MSG)

  line_up_po.inputName(user_name)
  line_up_po.inputNotes(user_note)
  line_up_po.changeNumberOfAdult(5)
  line_up_po.changeNumberOfChild(6)
  assertCheckPoint(browser, 'TID_008_3', TEST_ERR_MSG)

  # Close the info page, check the number at top right screen again
  # Observe

  # line_up_po.updateLineUpTicket()
  # WORKAROUND: [Bug #70] After user performed lineup, click cart icon & click menu icon will navigate to lineup page
  # browser.get(URL_FOOD_MENU_PAGE)

  # TODO: remove me
  # line_up_po.tapTopLeftCloseButton()
  line_up_po.submitLineUpTicket()
  assertCheckPoint(browser, 'TID_008_4', TEST_ERR_MSG)

  dialogue_po.tapOkButtonOnDialogue()
  assertCheckPoint(browser, 'TID_008_5', TEST_ERR_MSG)
  # WORKAROUND: [Bug #70] After user performed lineup, click cart icon & click menu icon will navigate to lineup page

  json_metadata['TID_008'] = 'skip with #072'
