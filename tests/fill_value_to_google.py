import os,sys
import gspread
from datetime import datetime
from pprint import pprint
import json
import string
from time import sleep
import pytz

TXT_RESULT_NOT_FOUND='ASK LOUIS'
REPORT_JSON_FILEPATH='./.report.json'
WORKBOOK_TO_FILL="[result] E-Order Smoke Test Plan"
SHEET_TO_FILL='Test Case'

gc = gspread.service_account()

sh = gc.open(WORKBOOK_TO_FILL)

in_json = ''.join(open(REPORT_JSON_FILEPATH,'r').readlines())
raw_result_json = json.loads(in_json)


def parseToTestIdAndResult():
  test_id_and_result_json={}
  for test_value in raw_result_json['tests']:
    test_id = test_value['metadata']['TEST_ID']
    test_result = test_value['outcome']
    test_id_and_result_json[test_id]=test_result
  return test_id_and_result_json

def fillNewDate(column_to_fill):
  datetime_now = datetime.now()
  # string_to_fill=datetime.now().strftime('%Y-%m-%d %H:%M')
  timezone = pytz.timezone("Asia/Hong_Kong")
  d_aware = timezone.localize(  datetime_now)
  string_to_fill=d_aware.strftime('%Y-%m-%d %H:%M')

  sh.sheet1.update_cell(ROW_DATETIME, column_to_fill, string_to_fill)

def findEmptyCellInRow(row=1):
  for i in range(2,1000):
    cell_value=sh.sheet1.cell(row, i).value
    if cell_value=='':
      return i

test_id_and_result_json=parseToTestIdAndResult()
# test_id_and_result_json = {
#   'TID_001': 'failed',
#   'TID_002': 'failed',
#   'TID_003': 'failed',
#   }

ROW_DATETIME=4
NEW_COLUMN_NUM=findEmptyCellInRow(ROW_DATETIME)

fillNewDate(NEW_COLUMN_NUM)

COL_TID_NAME=14
count_to_exit=0
exit_when_larger_than=4

def checkIfNeedToExit(count_to_exit, exit_when_larger_than):
    if count_to_exit > exit_when_larger_than:
      print('count to exit {} > {}, exitting'.format(count_to_exit ,exit_when_larger_than))
      sys.exit()

# vertical scanning
# google limit read rate applied
# https://gspread.readthedocs.io/en/latest/user-guide.html
for i in range(5,150):
  sleep(0.2)
  test_id_on_sheet=sh.sheet1.cell(i, COL_TID_NAME).value

  # if test_id_on_sheet=='':
  #   print("empty found, update done ?")
  #   break

  try:

    test_id_on_sheet=test_id_on_sheet.upper()
    test_result = test_id_and_result_json[test_id_on_sheet].upper()
    # sh.sheet1.update_cell(row,  column, testname)
    print('test_id_on_sheet {} found on row {}, filling result {} on col {}'.format(test_id_on_sheet, i, test_result, NEW_COLUMN_NUM))
    sh.sheet1.update_cell(i, NEW_COLUMN_NUM, test_result)

    # value found, reset count_to_exit
    count_to_exit=0

  except Exception as e:
    # currently either empty cell or cell TID not found
    if test_id_on_sheet=='':
      count_to_exit +=1
      print('cell is empty, raise count to exit +1, current count {}'.format(count_to_exit))
      checkIfNeedToExit(count_to_exit, exit_when_larger_than)

    else:
      print('test id not found, test id in spread sheet is {}'.format(test_id_on_sheet))
      sh.sheet1.update_cell(i, NEW_COLUMN_NUM, TXT_RESULT_NOT_FOUND)
  finally:
    checkIfNeedToExit(count_to_exit, exit_when_larger_than)
