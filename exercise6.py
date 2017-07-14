#!/usr/bin/env python

import  math

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    l = len(word)
    if l <= 1:
        return True
    elif first(word) != last(word):
        return False
    else:
        return is_palindrome(middle(word))

def gcfd(a,b):
    if a % b == 0:
        return b
    return gcfd(b, a % b)

print(is_palindrome('redivider'))

print(gcfd(12,18))

