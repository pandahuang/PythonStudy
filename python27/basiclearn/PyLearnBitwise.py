# -*- coding: utf-8 -*-
__author__ = 'panda_huang'
import functools

int2 = functools.partial(int, base=2)
print 'int2 value is : %d' % int2('101011001')
