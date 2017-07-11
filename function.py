#!/usr/bin/env python

def do_twice(func,arg):
    func(arg)
    func(arg)

def print_str(arg):
    print(arg)

def do_twice2(func):
    func()
    func()

def print_str2():
    print('ooo')

do_twice(print_str,'sss')
do_twice2(print_str2)