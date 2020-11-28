#!/usr/bin/env python

import os,sys
from pprint import pprint
import json

import requests
from stubs.server.config import *

json_raw='{"lid":"5fb7f0f17f11c030c1f30cea","seat":"3"}'
payload_json = json.loads(json_raw)

cookies = dict(manage_token=MANAGE_TOKEN)

try:

  r = requests.post(LIST_TABLE_URL_ASSIGN_TABLE,cookies=cookies, json=payload_json)

  if r.status_code != 200:
    raise Exception(ERR_END_POINT_NOT_REACHABLE)

  print(r.text)

except Exception as e:
  pass
