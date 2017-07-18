#!/usr/bin/env python
import os
import dbm
import pickle

'''
os.getcwd()
os.path.abspath(filename)
os.path.exists(fielname)
os.path.isdir(filename)
os.path.isfile(filename)
os.path.join(dirname,name)
'''

fout = open('output.txt','w')
line1 = 'This is the line one\n'
fout.write(line1)
line2 = 'This is the line two\n'
fout.write(line2)
fout.close()
fout = open('output.txt')
for line in fout:
    print(line.strip())

fout.close()
try:
    fin = open('bad_file')
except:
    print('Somethong went wrong')

db = dbm.open('capthon','c')
db['cleese.png'] = 'photo of John cleese'

db.close()
cwd = os.getcwd()
nb = 2
print('%(number)d is two' % {'number':nb})

t = [1,2,3,4]
s = pickle.dumps(t)
t1 = pickle.loads(s)

filename = 'output.txt'
cmd = 'ls -l'
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
st = '1 2\t 3\n 4'
print(repr(st))
print(res,stat)