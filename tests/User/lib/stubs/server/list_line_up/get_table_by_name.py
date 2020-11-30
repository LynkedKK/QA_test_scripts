#!/usr/bin/env python3

import os,sys
from pprint import pprint
import json

import requests

from list_all_table import listAllTable

def getTableByName(queue_user_name):
  all_table_json = listAllTable()
  all_table_by_name={}
  for table_json in all_table_json:
    all_table_by_name[table_json['name']]={
      'lid': table_json['lid']
      }

  return all_table_by_name[queue_user_name]

if __name__ == '__main__':
  print(getTableByName('louis_finger_print_1'))
