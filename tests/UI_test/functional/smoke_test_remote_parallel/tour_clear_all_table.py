import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *

from steps import *
from pages.config import *
from jp import *

from stubs.server.assign_table.assign_table_by_name import assignTableByName
from stubs.server.assign_table.assign_all_table import assignAllTable

# todo: factorize me
from urls import *

from setupLocalChrome import *

from test_TID_033 import *
# from test_TID_006 import *


def tour_clear_all_table(json_metadata):

  assignAllTable('TID.*')

  return 1
