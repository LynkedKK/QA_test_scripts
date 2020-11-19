import os,sys
from pprint import pprint
from diffimg import diff

def assertSameImage(img_expected, img_actual,image_test_threshold=0.05, error_msg='same image is expected but diff image found'):
  ''' exception if different image '''
  print("debug: diff result {}".format(diff(img_expected, img_actual)))
  print("debug: image_test_threshold {}".format(image_test_threshold))
  print("debug: diff assert diff result {}".format(diff(img_expected, img_actual) < image_test_threshold))
  assert diff(img_expected, img_actual) < image_test_threshold, error_msg + "debug: diff result {}".format(diff(img_expected, img_actual))
