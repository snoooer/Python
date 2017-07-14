#!/usr/bin/env python

fruit = 'banana'


def every(list):
    a = list
    n = len(a) - 1
    while n >= 0:
        print(a[n])
        n = n - 1

for letter in fruit:
    print(letter)

preeees = 'JKLMNOPQ'
sss = 'ack'

for preee in preeees:
    if preee == 'O' or preee == 'Q':
        print(preee+'u'+sss)
    else:
        print(preee+sss)

def find(word,letter,n):
    l = len(word)
    i = 0
    while n < l :
        if word[n] == letter:
            i = i + 1
        n = n + 1
    return i

def count_letter(word,letter):
    l = len(word)
    count = 0
    i = 0
    while i < l:
        if word[i] == letter:
            count = count + 1
        i = i + 1
    return count

def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    list = ''
    for letter in word:
        list += rotate_letter(letter, n)
    return list

if __name__ == '__main__':
    print(rotate_word('uVwxyza',-12))