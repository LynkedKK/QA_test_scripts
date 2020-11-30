import os,sys
from pprint import pprint

def get_current_test():
  return os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]