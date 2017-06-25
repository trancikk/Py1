import serial
import network2
import person
import Tkinter
import SimpleDialog 
import tkMessageBox
import person
import numpy as np

net=serial.load('nets_new_large_2_2')
def calculate(row):
    return (net[0][0].feedforward(row));

#print net[0][0]
test2=serial.load('success_norm')
test=serial.load('fail_norm')
#print [i.getNormalGen() for i in test]
#print '\n'
#print [i.printGens() for i in test]
#print '\n'
#print [i.getNormalGen() for i in test2]
#print test[0].getRow()
#print test2[0].getRow()
#print test[0].getNormalGen()
#print test[0].getResult()
print '\n cool1'
test_norm1=(test[2].getNormalGen())
print '\n'
test_norm2=[test[2].getRow()[i] for i in  sorted((test[0].getRow()).keys())]
print test_norm1
print test_norm2
#res=calculate(test_norm1[0])
res=calculate([1,2,3,4,5,6,7,8,9])
resa=net[0][0].accuracy([(list(test[8].getNormalGen()),1)])
#print res
#print '\n cool'
print res
#import genini
#import gen
#print ['Keys- %s, value - %s;' % (genini.gens[i].getName(), genini.gens[i].getGens()) for i in genini.gens.keys()]
#print [i.printNormGens() for i in test]