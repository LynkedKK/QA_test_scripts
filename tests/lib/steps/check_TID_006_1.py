
from config import *
from assert_check_point import assertCheckPoint
import table_assigned_dialogue
from time import sleep
import random

from stubs.server.assign_table.assign_table_by_name import assignTableByName

def run_check(json_metadata, browser, table_username ,sleep_before_confirm_s=20):
  TEST_ERR_MSG='User should automatically direct to food menu page with a number display dialog'

  # TODO: resume me
  # assertCheckPoint(browser, 'TID_006_1_1', TEST_ERR_MSG)

  assignTableByName(table_username, random.randrange(2,50,3))

  sleep(sleep_before_confirm_s)
  table_assigned_dialogue_po = table_assigned_dialogue.Main(browser)
  table_assigned_dialogue_po.tapOkButtonOnDialogue()

  # NOTE: update threshold due to table number varying
  assertCheckPoint(browser, 'TID_006_1_2', TEST_ERR_MSG, 0.05)

  json_metadata['TID_006_1'] = 'passed'
