#!/usr/bin/env python

def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print(letter)

def is_reverse(word1,word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j > 0:
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    return True

def any_lowcase(s):
    for c in s:
        flag = c.islower()
        print(flag)

any_lowcase('abA')