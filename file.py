#!/usr/bin/env python

file = open('test.txt','w')
file.write("Hello,world!")
file.close()
file = open('test.txt','r')
print(file.readlines())
file.close()
file = open('test.txt','r')
print(file.readline())