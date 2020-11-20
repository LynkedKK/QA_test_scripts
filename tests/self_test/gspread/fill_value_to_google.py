import os,sys
import gspread
from datetime import datetime
from pprint import pprint
import json

import pytz

TXT_RESULT_NOT_FOUND='ASK LOUIS'

gc = gspread.service_account()

sh = gc.open("Example spreadsheet")

in_json = ''.join(open('./tests/self_test/gspread/.report.json','r').readlines())
raw_result_json = json.loads(in_json)


def parseToTestIdAndResult():
  test_id_and_result_json={}
  for test_value in raw_result_json['tests']:
    test_id = test_value['metadata']['TEST_ID']
    test_result = test_value['outcome']
    test_id_and_result_json[test_id]=test_result
  return test_id_and_result_json

# result_json = {
#   'TID_FAIL01': 'failed',
#   'TID_FAIL02': 'failed',
#   'TID_FAIL03': 'failed',
#   'TID_PASS01': 'passed',
#   'TID_PASS02': 'passed',
#   'TID_PASS03': 'passed',
#   'TID_PASS04': 'passed',
#   'TID_PASS05': 'passed'
#   }

def fillNewDate(column_to_fill):
  datetime_now = datetime.now()
  # string_to_fill=datetime.now().strftime('%Y-%m-%d %H:%M')
  timezone = pytz.timezone("Asia/Hong_Kong")
  d_aware = timezone.localize(  datetime_now)
  string_to_fill=d_aware.strftime('%Y-%m-%d %H:%M')

  sh.sheet1.update_cell(1, column_to_fill, string_to_fill)

def findEmptyCellInRow(row=1):
  for i in range(2,1000):
    cell_value=sh.sheet1.cell(row, i).value
    if cell_value=='':
      return i

test_id_and_result_json=parseToTestIdAndResult()

NEW_COLUMN_NUM=findEmptyCellInRow()

fillNewDate(NEW_COLUMN_NUM)

for i in range(2,150):
  test_id_on_sheet=sh.sheet1.cell(i, 1).value

  if test_id_on_sheet=='':
    print("empty found, update done ?")
    break

  try:
    test_id_on_sheet=test_id_on_sheet.upper()
    test_result = test_id_and_result_json[test_id_on_sheet].upper()
    # sh.sheet1.update_cell(row,  column, testname)
    print('test_id_on_sheet {} found on row {}, filling result {} on col {}'.format(test_id_on_sheet, i, test_result, NEW_COLUMN_NUM))
    sh.sheet1.update_cell(i, NEW_COLUMN_NUM, test_result)

  except Exception as e:
    print('test id not found, test id in spread sheet is {}'.format(test_id_on_sheet))
    sh.sheet1.update_cell(i, NEW_COLUMN_NUM, TXT_RESULT_NOT_FOUND)
