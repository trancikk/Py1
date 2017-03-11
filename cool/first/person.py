# -*- coding: utf-8 -*-
import sys
from test.leakers import test_selftype
reload(sys)
sys.setdefaultencoding('utf-8')
class Person(object):
    


    def __init__(self, args,firstRow):
        self.gens=dict(zip(firstRow,args))
        self.surname=self.gens[u'\u0424\u0418\u041e'].split()
    def getProp(self):
        return self.gens
    def setProp(self,value,row):
        self.prop[row]=value
     
    def setResult(self,row):
        self.result=row[u'\u0414\u0438\u0430\u0433\u043d\u043e\u0437']
    def getRow(self):
        return self.gens
    def getSurname(self):
        return self.surname[0]   
    def getResult(self):
        return self.result