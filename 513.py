#!/usr/bin/env python
import math

def is_angle(a,b,c):
    list = [a,b,c]
    list.sort()
    if int(list[0]) + int(list[1]) > int(list[2]):
        print("yes")
    else:
        print("no")

def area(r):
    s = math.pi*r**2
    return s

def compose(x,y):

    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0

def distance(x1,y1,x2,y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    dis = dy**2 + dx**2
    result = math.sqrt(dis)
    s = area(result)
    return s
print(distance(1,2,3,4))
a = input("a=\n")
b = input("b=\n")
c = input("c=\n")
is_angle(a,b,c),
res = compose(2,3)
s = area(2)
print("s = {:.4f} res = {}".format(s,res))

