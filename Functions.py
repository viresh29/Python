import os
import sys

p = os.path.join('C:/','Users/viresh.patel/Documents/QA Test Plan')

print(os.listdir(p))
print(sys.platform)
print(list(os.environ.items()))