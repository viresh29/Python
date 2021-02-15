import os
from datetime import datetime


# print(dir(os))
# get current working directory
# print(os.getcwd())

# change current working directory
# Create directory
# create sub directory
# remove directory
# rename directory or file
# os.stat  --> get the info of the file like size, when It created etc..
# os.walk  --> generator tuple 3 directory

"""
for dirpath, dirnames, filenames in os.walk('/Users/viresh.patel/PycharmProjects/Python'):
    print('Current Path: ',dirpath)
    print('Directories:',dirnames)
    print('Files',filenames)
    print()
"""

file_path = os.path.join('./export/GoogMaps_', str(datetime.now()), '.csv')
print(file_path)
