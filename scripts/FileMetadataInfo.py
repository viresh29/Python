import os
import csv


zFile = 'C:\\Users\\viresh.patel\\Documents\\Excel Docs\\global_superstore.csv'
zInfo = os.stat(zFile)

print(zInfo)
print(zInfo.st_atime)
print(zInfo.st_ctime)
print(zInfo.st_dev)
# print(zInfo.st_file_attributes)
print(zInfo.st_gid)
print(zInfo.st_ino)
print(zInfo.st_mode)
print(zInfo.st_mtime)
print(zInfo.st_nlink)
print(zInfo.st_size)
print(zInfo.st_uid)


for zLang in csv.list_dialects():
    print(zLang)

zFileR = open(zFile, 'r')
reader = csv.reader(zFileR)
for line in reader:
    if len(line) != 0:
        print(line[0])
zFileR.close()
