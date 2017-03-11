# -*- coding: utf-8 -*-
import excel
import locale
import sys
import serial
from matplotlib.pyplot import cool
from dask.tests.test_multiprocessing import bad
reload(sys)
sys.setdefaultencoding('utf-8')
#locale.setlocale(locale.LC_ALL, "ru_RU")
print sys.stdout.encoding
a=excel.ExcelFile('1.xlsx')
b=excel.ExcelFile('Control group 2.xlsx')
c=excel.ExcelFile('Fetus 2.xlsx')
print(c.getRow(2))
serial.serialise(c,'cool')
good=serial.load('cool')
head=good.getRow(0)
print head[2]
if good.getRow(2)[2]=='CT':
    print 'cool'
else:
    print 'bad'

