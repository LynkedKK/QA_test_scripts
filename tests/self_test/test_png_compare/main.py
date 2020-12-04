import os,sys
from pprint import pprint

HOME_DIR='/home/logic/_workspace/LynkedKK/QA_test_scripts_master/tests'
SELF_TEST_DIR=os.path.abspath(HOME_DIR+'/..')
TEST_HOME=os.path.abspath(SELF_TEST_DIR+'/tests')
# LIB_DIR=os.path.abspath(SELF_TEST_DIR+'/lib')
print(TEST_HOME)
sys.path.append(TEST_HOME)

from lib.asserts.assert_image import assertSameImage

EXPECTED_DIR='/home/logic/_workspace/LynkedKK/QA_test_scripts_master/tests/UI_test/functional/smoke_test_remote_parallel/expected'

print(
  assertSameImage(
    EXPECTED_DIR+'/TID_036_4_sc.png',
    '/home/logic/_del/1/TID_036_4_sc_23.png'
  )
)
