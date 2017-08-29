__author__ = 'panda_huang'
import os
import sys

files = os.listdir('C:\\Users\\panda_huang\\Desktop\\PR\\Assignment3\\TJ_Faces\\444')

count = 1
i = 4
for name in files:
    newname = str(i) + '_' + str(count) + '.jpg'
    count = count + 1
    os.chdir('C:\\Users\\panda_huang\\Desktop\\PR\\Assignment3\\TJ_Faces\\444')
    os.rename(name, newname)
