#!/usr/bin/env python

cheeses = ['Cheddra','Edam','Gouda']

numbers = [43,123]

empty = []

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
def bad_del_head(t)
    
t = ['a','b','c','E','e','f']
x = t.pop(2)
print(x)
del t[0]
t.remove('e')
s = 'Python is good'
s1 = s.split()
t1 = ' '.join(s1)
print(t1)