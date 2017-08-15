import os
import sys

p = os.path.join('C:/','Users/viresh.patel/Documents/QA Test Plan')

print(os.listdir(p))
print(sys.platform)
print(list(os.environ.items()))


for param in os.environ.keys():
    print(param,os.environ[param])


print(os.getcwd())
print(os.listdir(os.curdir))
print(os.chdir('C:/Users/viresh.patel/Documents/QA Test Plan'))
print(os.getcwd())


