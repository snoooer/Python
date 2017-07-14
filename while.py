#!/usr/bin/env python

def countdown(n):
    while n > 0 :
        print(n)
        n = n - 1
    print(0)

def sequence(n):
    while n != 1 :
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

def print_n(s,n):
    while n > 0 :
        print(s)
        n = n - 1
    print(s)

while True :
    line = input('>')
    if line == 'done':
        print(line)
        break
    print('Done')