import os,sys
from pprint import pprint
from datetime import datetime
import hashlib

def getTimeNowMd5(datetime_now):
  print(hashlib.md5(datetime_now.encode('utf-8')).hexdigest())

if __name__=="__main__":
  datetime_now=datetime.now().strftime('%Y%m%D%H%M%S')
  getTimeNowMd5(datetime_now)