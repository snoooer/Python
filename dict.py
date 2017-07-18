#!/usr/bin/env python

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

res = 1

def change_res():
    global res
    res = res + 1
    print(res)

en2sp = dict()

en2sp['one'] = 'uno'
en2sp['two'] = 'docs'
en2sp['three'] = 'tres'
en2sp['two'] = 'dos'
s = 'banana'
vals = en2sp.values()
print(histogram(s))
change_res()