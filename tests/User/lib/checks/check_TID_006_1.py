import random

import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page
import lib.pages.table_assigned_dialogue as table_assigned_dialogue

from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import *

from lib.stubs.server.assign_table.assign_table_by_name import assignTableByName


def run_check(json_metadata, browser, table_username ,sleep_before_confirm_s=10):
  TEST_ERR_MSG='User should automatically direct to food menu page with a number display dialog'

  assertCheckPoint(browser, 'TID_006_1_1', TEST_ERR_MSG)

  assignTableByName(table_username, random.randrange(2,50,3))

  sleep(sleep_before_confirm_s)
  table_assigned_dialogue_po = table_assigned_dialogue.Main(browser)
  table_assigned_dialogue_po.tapOkButtonOnDialogue()

  assertCheckPoint(browser, 'TID_006_1_2', TEST_ERR_MSG)

  json_metadata['TID_006_1'] = 'passed'
