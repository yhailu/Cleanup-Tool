import os
from os.path import join
import shutil
import sys
import time
list = []
import re

destinationdir = join('C:', '\Users', 'yhailu', 'Desktop', 'u_drive_cleanup')
print destinationdir
if os.path.exists(destinationdir):
    pass
else:
    os.makedirs(destinationdir)


time.sleep(5)
str1 = '6.0.8.15.3'

sourcedir = 'C:\Users\yhailu\Downloads\u_drive_cleanup\TPS_60_Client/'
lis = os.listdir(sourcedir)
for x in lis:
    if x.endswith('.zip'):
        if re.search(str1, x):
            print 'found it'
            continue
        else:
            shutil.move(sourcedir + x, destinationdir)