#coding:utf-8
#!/usr/bin/env python
"readTextFile.py -- read and display text file"

import os

#get filename
filename = raw_input("Enter filename:")
curpath = os.path.abspath(os.curdir)
fname = curpath + r'\test'+ r'\\' + filename
print fname

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** File open error:", e
else:
    # display contents to the screen
    for eachLine in fobj:
        print eachLine
    fobj.close()
