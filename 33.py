#!/usr/bin/env python

def print_plus():
    print('+'+'-'*4+'+'+'-'*4+'+')

def print_shu():
    print('|'+' '*4+'|'+' '*4+'|')

def do_four(func):
    func()
    func()
    func()
    func()

print_plus()
do_four(print_shu)
print_plus()
do_four(print_shu)
print_plus()