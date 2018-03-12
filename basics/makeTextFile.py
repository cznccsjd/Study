#coding:utf-8

"makeTextFile.py --create text file"

import os
ls = os.linesep

# get filename
while True:
    cur_path = os.path.abspath(os.curdir)   #获取当前路径
    filename = raw_input("\nPlease Enter filename:\n")  #注意这里是python2.7的用法，3.X需要用input
    print filename
    fname = cur_path + r'\test' + r'\\' + filename
    print fname

    if os.path.exists(fname):
        print "\nERROR:'%s' already exists" % fname
    else:
        break

#get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

#loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line=ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'DONE!'
