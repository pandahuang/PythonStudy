# -*- coding: utf-8 -*-
__author__ = 'panda_huang'


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n = n + 1
        yield b


def fib1():
    a, b = 0, 1
    a, b = b, a + b
    yield b
    a, b = b, a + b
    yield b
    a, b = b, a + b
    yield b
    a, b = b, a + b
    yield b


ftemp = fib1

print list(fib1())

for n in fib(6):
    print(n)
