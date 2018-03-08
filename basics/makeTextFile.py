#coding:utf-8

"makeTextFile.py --create text file"

import os
ls = os.linesep

# get filename
while True:

    if os.path.exists(fname):
        print "ERROR:'%s' already exists" % fname
