import os
from os.path import join
import sys

os.chdir(join(os.environ["SKYSPACE"], "posts"))

try:
  category_name = sys.argv[1]
except:
  category_name = input("category name?\n>> ")

os.mkdir(category_name)
os.mkdir(join(category_name, "src"))
os.mkdir(join(category_name, "src", "compiled"))
os.mkdir(join(category_name, "src", "images"))
