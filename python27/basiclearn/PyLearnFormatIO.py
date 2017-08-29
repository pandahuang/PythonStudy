# -*- coding: utf-8 -*-
__author__ = 'panda_huang'
intvalue = 35
floatvalue = 35.35
strvalue = 'Lijinjin'
chavalue = u'李瑾瑾'

print('Int Value is : %d' % intvalue)
print('Int Value is : %06d' % intvalue)
print('Float Value is : %f' % floatvalue)
print('Float Value is : %.2f' % floatvalue)
print('String Value is : %s' % strvalue)
print('String Value is : %9s' % strvalue)
print('String Value is : %-9s' % strvalue)
print('Chinese Value is : %s' % chavalue)

print('Format Value is : %-s' % format(0.000035, '.2e'))
