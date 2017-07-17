#!/usr/bin/env python

def is_abcd(word):
    l = len(word) - 1
    i = 0
    while i < l :
        if word[i + 1] < word[i]:
            return False
        i += 1
    return True


print(is_abcd('a'))