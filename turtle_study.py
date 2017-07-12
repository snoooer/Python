#!/usr/bin/env python

import turtle
import math

bob = turtle.Turtle()
''''
for i in range(4):
    print('hello')
    bob.fd(100)
    bob.lt(90)
'''
def polygon(t,length,n):

    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def polyline(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t,r,angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t,n,step_length,step_angle)

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def circle(t,r):
    arc(t,r,360)

circle(bob,200)

turtle.mainloop()