# -*- coding: utf-8 -*-
__author__ = 'panda_huang'


# normal sum()
def normalSum(*numlist):
    def add(x, y):
        return x + y

    return reduce(add, numlist)


total = normalSum(1, 2, 3, 4, 5)
print total


# lazy sum()
def lazySum(*numlist):
    def sum():
        total = 0
        for num in numlist:
            total = total + num
        return total

    return sum


print lazySum(1, 2, 3, 4, 5)()


# Closure
# cyclic variable wrong
def countW():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# f1, f2, f3 = countW()
# print f1()
# print f2()
# print f3()

# cyclic variable right
def countR():
    fs = []
    for i in range(1, 4):
        def f(j):
            return lambda: j * j
            # def g():
            #     return j*j
            # return g

        fs.append(f(i))
    return fs


f1, f2, f3 = countR()
print f1()()
print f2()
print f3()
