
from step_helloworld import *
from assert_helloworld import *
from check_helloworld import *

def tour_helloworld(json_metadata):
  step_helloworld(json_metadata)
  assert_helloworld(json_metadata)
  check_helloworld(json_metadata)

  print('helloworld')
