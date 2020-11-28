import os,sys
from pprint import pprint

from time import sleep


list_file_as_module=map(lambda y: y.replace('.py',''), filter(lambda x: x!='__init__.py', os.listdir('./tests/lib/steps')))

# pprint(list(list_file_as_module))
# assert False,'findme'

__all__=list(list_file_as_module)
