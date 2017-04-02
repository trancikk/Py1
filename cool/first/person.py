# -*- coding: utf-8 -*-
import sys
from test.leakers import test_selftype
import serial
reload(sys)
sys.setdefaultencoding('utf-8')
data_gens=serial.load('gens_dict')
class Person(object):
    


    def __init__(self, args,firstRow):
        self.gens=dict(zip(firstRow,args))
        self.surname=self.gens[u'\u0424\u0418\u041e'].split()
        
    def printGens(self):
        for i in self.gens:
            print 'Key - %s, value - %s; ' % (i, self.gens[i])
            
    def printNormGens(self):
        for i in self.gens_normalise:
            print 'Key - %s, value - %s; ' % (i, self.gens_normalise[i])
    
    def getProp(self):
        return self.gens
    
    def setProp(self,value,row):
        self.prop[row]=value
     
    def setResult(self,row):
        self.result=row[u'\u0414\u0438\u0430\u0433\u043d\u043e\u0437']
        
    def getRow(self):
        return self.gens
    
    def setRow(self,row):
        self.gens_normalise=list(row)
    
    def getNormalGen(self):
        return self.gens_normalise
        
    def getSurname(self):
        return self.surname[0]
       
    def getResult(self):
        try:
            return self.result
        except AttributeError:
            self.result='B'
            return 'В'
        
    def normaliseGens(self,example):
        for i in sorted(self.gens.keys()):
            if i not in example:
                self.gens.pop(i)
        self.setRow(data_gens[i].normalise(i,self.getRow()[i]) for i in sorted(self.gens.keys()))
                         
    def normaliseResults(self):
        if self.getResult()=='НВ':
            self.result=0
        else:
            self.result=1
