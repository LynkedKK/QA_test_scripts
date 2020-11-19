import os,sys
from pprint import pprint
from diffimg import diff

SELF_TEST_DIR=os.path.dirname(__file__)
TEST_ROOT=os.path.abspath(SELF_TEST_DIR+'/..')
LIB_DIR=os.path.abspath(TEST_ROOT+'/lib')
LIB_ASSERT_DIR=os.path.abspath(LIB_DIR+'/asserts')

sys.path.append(LIB_ASSERT_DIR)

from assert_image import assertSameImage

HELLOWORLD_A_PNG='tests/self_test/helloworld_a.png'
HELLOWORLD_B_PNG='tests/self_test/helloworld_b.png'

TEST_PAIR_0_5_A='tests/self_test/assert_image_test_pair/0.5/test_happyflow_1_chrome_first_time_landing_iphonex_a.png'
TEST_PAIR_0_5_B='tests/self_test/assert_image_test_pair/0.5/test_happyflow_1_chrome_first_time_landing_iphonex_b.png'


def test_hello_diffimg():
  assert diff(HELLOWORLD_A_PNG, HELLOWORLD_A_PNG)==0, 'same image output not correct'
  assert diff(HELLOWORLD_A_PNG, HELLOWORLD_B_PNG)!=0, 'diff image output not correct'

def test_assert_image_testCall():
  assertSameImage(TEST_PAIR_0_5_A, TEST_PAIR_0_5_B, 0.1, 'hello error message')

  pass