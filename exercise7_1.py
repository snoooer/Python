#!/usr/bin/env python
import  math

def mysqrt(a):
    x = 1
    while True :
        y = (x + a / x) / 2
        if abs(y - x) < 0.0000000000000000001 :
            break
        x = y
    x = y
    return x

def diff(n):
    r = abs(mysqrt(n) - math.sqrt(n))
    print("r = {},mysqrt = {},math.sqrt = {}".format(r,mysqrt(n),math.sqrt(n)))

def eval_loop():
    t = 0
    while True :
        a = input(">")
        line = 'done'
        if a == line:
            break
        t =t + eval(a)
    print(t)

print(eval('1+3+4'))
diff(90)

eval_loop()