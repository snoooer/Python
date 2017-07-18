#!/usr/bin/env python

def min_max(t):
    return min(t),max(t)

def print_all(*args):
    return args

def sumall(*args):
    count = 0
    for arg in args:
        count = count + arg
    return count

t = [1,2,3,4]
s = 'abcd'
for pair in zip(s,t):
    print(pair)