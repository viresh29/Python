import os
import sys



my = open('C:/Files/test.txt','w')
my.write('Hello world!\n')
my.close()

f = open('C:/Files/test.txt')
f.seek(0)
print(f.read())
f.close()