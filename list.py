#!/usr/bin/env python

letters = ['a','b','c','d','e','f']

letters.append('h')
print(letters)
a = ['a','b','c']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0])
print(x[1][2])

x1,x2 = 0,1
while x2 < 10:
    print(x2,end=',')
    x1,x2 = x2,x1 + x2