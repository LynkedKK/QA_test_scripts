import os,sys
import re
from pprint import pprint
import json
import random

import requests
from stubs.server.config import *
from stubs.server.assign_table.list_all_table import listAllTable

from stubs.server.assign_table.assign_table_by_lid import assignTableByLid

def assignAllTable(name_pattern='TID_.*', seat='1'):
  name_pattern = re.compile('({})'.format(name_pattern))
  try:
    pending_list = listAllTable()
    for pending in pending_list:
      m = re.match(name_pattern, pending['name'])
      if (m is not None):
        if ( len(m.groups()) > 0):
          # assert False, 'assign table by tid {}'.format(pending['lid'])
          assignTableByLid(pending['lid'], seat)
      # assert False, 'hello fail'
  except Exception as e:
    # pprint(pending_list)
    # pprint(m)
    raise e
    # pass

if __name__=="__main__":
  assignAllTable()
  # assignTableByName('louis_finger_print_1')