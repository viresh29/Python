import importlib
from os import path
from camelcase import CamelCase
from params import XYZ
import mymodule

mymodule.greeting('viresh')

c = CamelCase()

dag_name = path.basename(path.dirname(__file__))
xyz = importlib.import_module('params')

txt = 'hello world'
print(c.hump(txt))

print(xyz.XYZ)
