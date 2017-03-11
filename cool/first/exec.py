# -*- coding: utf-8 -*-
import excel
import locale
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#locale.setlocale(locale.LC_ALL, "ru_RU")
print sys.stdout.encoding
a=excel.ExcelFile('1.xlsx')
b=excel.ExcelFile('Control group 2.xlsx')
c=excel.ExcelFile('Fetus 2.xlsx')
print(c.getRow(2))

