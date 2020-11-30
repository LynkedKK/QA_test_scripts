import os,sys
from pprint import pprint
import json
import random

import requests
from stubs.server.config import *

def assignTableByLid(lid, seat):
  json_raw='{"lid":"'+lid+'","seat":"'+str(seat)+'"}'
  payload_json = json.loads(json_raw)

  cookies = dict(manage_token=MANAGE_TOKEN)

  try:
    r = requests.post(LIST_TABLE_URL_ASSIGN_TABLE,cookies=cookies, json=payload_json)
    if r.status_code != 200:
      raise Exception(ERR_END_POINT_NOT_REACHABLE)

    # print(r.text)
  except Exception as e:
    raise e

if __name__=="__main__":
  assignTableByLid('5fb8c3c07f11c030c1f34ed1', random.randrange(2,50,3))
  # assignTableByName('louis_finger_print_1')