#!/usr/bin/env python

import os,sys
from pprint import pprint
import json
import random

from stubs.server.assign_table.get_lid_by_name import getLidByName
from stubs.server.assign_table.assign_table_by_lid import assignTableByLid


def assignTableByName(name, seat):
  print('helloworld')
  lid_by_name = getLidByName(name)
  target_lid = lid_by_name['lid']
  assignTableByLid(target_lid, seat)

if __name__=="__main__":
  assignTableByName('TID_019_USER', random.randrange(2,50,3))
