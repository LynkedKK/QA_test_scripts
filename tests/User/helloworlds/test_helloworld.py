import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *
from urls import *

# from tour_helloworld import *

from lib.steps.step_helloworld import *
from lib.asserts.assert_helloworld import *
from lib.checks.check_helloworld import *

def test_helloworld(json_metadata):
  step_helloworld(json_metadata)
  assert_helloworld(json_metadata)
  check_helloworld(json_metadata)

  print('helloworld')
