#!/usr/bin/env python3

import os,sys
from pprint import pprint
import json

import requests

from stubs.server.config import *

def listAllTable():

  cookies = dict(manage_token=MANAGE_TOKEN)
  r = requests.get(LIST_TABLE_URL, cookies=cookies)

  try:
    if r.status_code != 200:
      raise Exception('end point not reachable')

    # print(r.status_code)
    TABLE_LIST_TEXT=r.text
    TABLE_LIST_JSON = json.loads(TABLE_LIST_TEXT)

    # pprint(TABLE_LIST_JSON)
    # print(list(map(lambda x: x['lid'], TABLE_LIST_JSON)))

    return TABLE_LIST_JSON
  except Exception as e:

    pass

if __name__ == '__main__':
  listAllTable()