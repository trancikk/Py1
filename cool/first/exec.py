# -*- coding: utf-8 -*-
import excel
import locale
import sys
import serial
import person

reload(sys)
sys.setdefaultencoding('utf-8')
#locale.setlocale(locale.LC_ALL, "ru_RU")
#print sys.stdout.encoding
result=excel.ExcelFile('1.xlsx')
success=excel.ExcelFile('Control group 2.xlsx')
fail=excel.ExcelFile('Fetus 2.xlsx')
#print(.getRow(2))
#serial.serialise(c,'cool')
#good=serial.load('cool')
#head=good.getRow(0)
#firstRow=good.getRow(1)
#print head[2]
#if good.getRow(2)[2]=='CT':
#    print 'cool'
#else:
#    print 'bad'
successHead=success.getRow(0)
failHead=fail.getRow(0)
head=failHead[2:]
serial.serialise(head,'gens')
successPerson=list()
failPerson=list()
resultHead=result.getRow(0)
resultPerson=list()
for i in range(success.getNum()-1):
    successPerson.append(person.Person(success.getRow(i+1),successHead))
#    print i
for i in range(fail.getNum()-1):
    failPerson.append(person.Person(fail.getRow(i+1),failHead))
for i in range(result.getNum()-1):
    resultPerson.append(person.Person(result.getRow(i+1),resultHead))
#print resultHead[4:5]
#k=0   
for i in range(result.getNum()-1):
    for t in range(fail.getNum()-1):
        if failPerson[t].getSurname() == resultPerson[i].getSurname():
            failPerson[t].setResult(resultPerson[i].getRow())
            #print failPerson[t].getSurname(),resultPerson[i].getSurname(),resultPerson[i].getRow()[u'\u0414\u0438\u0430\u0433\u043d\u043e\u0437'], failPerson[t].getResult()
            #k+=1

serial.serialise(failPerson, 'fail')
serial.serialise(successPerson, 'success')
serial.serialise(resultPerson, 'result')

for i in failPerson:
    i.normaliseGens(head)
    i.normaliseResults() 
for i in successPerson:
    i.normaliseGens(head)
    i.normaliseResults()
serial.serialise(failPerson, 'fail_norm')
serial.serialise(successPerson, 'success_norm')
 
#print k
#personGood=person.Person(firstR)
##Person1=person.Person(firstRow,head)
#print((Person1.getProp()))
#print(Person1.getProp()[u'\u0424\u0418\u041e']);
