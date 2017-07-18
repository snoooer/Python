#!/usr/bin/env python

def nested_sum(t):
    count = 0
    for i in t:
        count += sum(i)
    return count

def cumsum(t):
    count = 0
    for i in range(len(t)):
        count = count + t[i]
        t[i] = count
    return t

def middle(t):
    return t[1:-1]


t = [1,2,3,4]

print(cumsum(t))
print(middle(t))