# -*- coding: utf-8 -*-
__author__ = 'panda_huang'
# get function through variable
import time


def nowTime():
    print time.localtime(time.time())
    print time.time()


f = nowTime
showtime = f()
print nowTime.__name__
print f.__name__


# print log simple
def log(func):
    def printer(*args, **kw):
        print 'call %s()' % func.__name__
        func(*args, **kw)

    return printer


def newLog(func):
    def printer(*args, **kw):
        print 'begin call %s()' % func.__name__
        func(*args, **kw)
        print 'end call %s()' % func.__name__

    return printer


def textLog(*text):
    def decorator(func):
        def printer(*args, **kw):
            print 'call %s() for %s' % (func.__name__, text)
            func(*args, **kw)

        return printer

    return decorator


@textLog()
def now(numlist):
    for num in numlist:
        print 'count is %10d' % num
    print time.time()


now([x for x in range(0, 10)])
