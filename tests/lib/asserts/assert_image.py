import os,sys
from pprint import pprint
from diffimg import diff

def assertSameImage(img_expected, img_actual,image_test_threshold=0.05, error_msg='same image is expected but diff image found'):
  ''' exception if different image '''
  img_diff_result = diff(img_expected, img_actual)
  verdict = img_diff_result < image_test_threshold
  check_point_name = os.path.basename(img_actual).replace('.png','')
  DEBUG_MSG = "debug: file: {}, threshold {}, diff result {}, verdict {}".format(img_actual, image_test_threshold, img_diff_result, verdict)
  print(DEBUG_MSG)
  assert verdict, check_point_name+' : ' +error_msg
