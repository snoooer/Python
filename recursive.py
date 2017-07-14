#!/usr/bin/env python

def is_between(x, y, z):
    if x <= y and y <= z:
        return True
    else:
        return False

def factorial(n):
    if not isinstance(n,int):
        print("xxxxx")
        return None
    elif n < 0:
        print("xx")
        return None
    elif n == 0:
        return 1
    else:
        result = n*factorial(n-1)
        return result

def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def ack(m,n):
    if not (isinstance(m,int) and isinstance(n,int)):
        print("xxx")
        return None
    if m < 0 or n < 0:
        print("ooooo")
        return None
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1,1)
    else:
        return ack(m - 1,ack(m,n - 1))

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


print(ackermann(4,3))
print(ack(3,4))