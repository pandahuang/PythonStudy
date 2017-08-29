# -*- coding: utf-8 -*-
__author__ = 'panda_huang'
f = abs


def addAbs(x, y, f):
    return f(x) + f(y)


print addAbs(1, -2, abs)


# map()
def strTrans(strA):
    strC = str.upper(strA[0]) + str.lower(strA)[1:]
    return strC


def strListTrans(strlist):
    return map(strTrans, strlist)


strlist = ['adam', 'LISA', 'barT']
strlistA = strListTrans(strlist)
print strlistA


# reduce()
def product2(x, y):
    return x * y


def productAll(numlist):
    return reduce(product2, numlist)


numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = productAll(numlist)
print num


def productAllSimple(numlist):
    return reduce(lambda x, y: x * y, numlist)


numS = productAllSimple(numlist)
print numS


# filter()
def isOdd(n):
    return n % 2 == 1


oddlist = filter(isOdd, [x for x in range(1, 11)])
print oddlist

# sorted()
sortedlist = sorted(strlist, key=str.lower)
print sortedlist
