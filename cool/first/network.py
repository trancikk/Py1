# -*- coding: utf-8 -*-
from pybrain.structure import FeedForwardNetwork
import serial
from pybrain.datasets import SupervisedDataSet
import person
from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer, RPropMinusTrainer

from pybrain.structure.modules   import SoftmaxLayer

from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal
import numpy as np
from pybrain.structure import LinearLayer, SigmoidLayer, BiasUnit
from pybrain.structure import FullConnection

from pybrain.tests.helpers import gradientCheck


#from first.numpy.core.defchararray import array
#TODO ?
n = FeedForwardNetwork()
dssuccess=serial.load('success_norm')
dsfail=serial.load('fail_norm')
head=serial.load('gens_list')
full=dsfail+dssuccess
alldata = ClassificationDataSet(9, 1, nb_classes=2)
#print len(dssuccess)
#print len(full)
#t=0
for i in (full):
    alldata.addSample(i.getNormalGen(),[i.getResult()])
    #print t
    #i.printGens()
    #print 'kkkeys -%s'%i.getProp().keys()
    #print i.getSurname()
    #print i.getResult()
    #t+=1
#ds=SupervisedDataSet(9,1)
#ds.addSample(inp, target)
alldata._convertToOneOfMany( )
tstdata,trndata  = alldata.splitWithProportion(0.15)
#valdata, trndata = netdata.splitWithProportion(0.10)

#trndata._convertToOneOfMany( )
print "Number of training patterns: ", len(trndata)
print "Input and output dimensions: ", trndata.indim, trndata.outdim
print "First sample (input, target, class):"
print trndata['input'][0], trndata['target'][0], trndata['class'][0]
#tstdata._convertToOneOfMany( )
inLayer = LinearLayer(9, name='in')
hiddenLayer = SigmoidLayer(15, name='hide')
bias1=BiasUnit(3)
hiddenLayer2 = SigmoidLayer(7, name='hide2')
#bias2=BiasUnit(7)
hiddenLayer3 = SigmoidLayer(3, name='hide3')
#bias3=BiasUnit(3)
outLayer = SoftmaxLayer(2, name='out')
n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addModule(hiddenLayer2)
n.addModule(hiddenLayer3)
n.addModule(bias1)
#n.addModule(bias2)
#n.addModule(bias3)
n.addOutputModule(outLayer)
in_to_hidden = FullConnection(inLayer, hiddenLayer, name = 'con1')
hidden1_to_hidden2 = FullConnection(hiddenLayer, hiddenLayer2, name = 'con2')
#bias1_to_hidden2 = FullConnection(bias1, hiddenLayer2, name='con2')
hidden2_to_hidden3 = FullConnection(hiddenLayer2, hiddenLayer3, name = 'con3')
hidden3_to_bias1 = FullConnection(bias1, hiddenLayer3, name='con3b')
#hidden3_to_bias_3 = FullConnection(hiddenLayer2, bias1, name = 'con3b')
bias3_to_out = FullConnection(hiddenLayer3, outLayer, name='con4')
n.addConnection(in_to_hidden)
n.addConnection(hidden1_to_hidden2)
#n.addConnection(bias1_to_hidden2)
n.addConnection(hidden2_to_hidden3)
#n.addConnection(bias2_to_hidden3)
n.addConnection(hidden3_to_bias1)
n.addConnection(bias3_to_out)
n.sortModules()
n.randomize()
print alldata

fnn = buildNetwork( trndata.indim, 5, trndata.outdim,hiddenclass=SigmoidLayer,bias=1, outclass=SigmoidLayer )
trainer = RPropMinusTrainer( n, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)#,batchlearning=True)
#trainer2 = RPropMinusTrainer( n, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.1,batchlearning=1)
for i in range(20):
    trainer.trainEpochs(30)
    #trainer2._checkGradient(trndata)
#trainer2.trainEpochs(2)
#trainer2.testOnClassData()
#trainer.trainUntilConvergence()
print n.activate(tstdata['input'][0])
print tstdata['target'][0]
print n.activate(trndata['input'][0])
print trndata['target'][0]
#print fnn.activate(tstdata['input'][0])
#print tstdata['target'][0]
#print fnn.activate(tstdata['input'][1])
#print tstdata['target'][1]
#print fnn.activate(tstdata['input'][2])
#print tstdata['target'][2]
#print fnn.activate(tstdata['input'][3])
#print tstdata['target'][3]
#print fnn.activate(tstdata['input'][4])
#print tstdata['target'][4]
#print fnn.activate(tstdata['input'][5])
#print tstdata['target'][5]

#pyplot.show()
#pyplot.show(pyplot.plot(tstdata['target']))
#pyplot.show(pyplot.plot(n.activateOnDataset(tstdata)))
#print ' =================\n'
#print n.activateOnDataset(tstdata)
#print tstdata

#print n.activate(trndata['input'][1])
#print trndata['target'][1]
#n.sortModules()
#print n
#print n.params
#print gradientCheck(n)
#serial.serialise(n,'network')
#print 'good'
#netw=serial.load('network')
#print netw
'''import network2
net = network2.Network([9, 15, 2], cost=network2.CrossEntropyCost)
net.large_weight_initializer()
training_data=list()
test_data=list()
for i in range(len(trndata)):
    arr=list()
    #np.ndarray(len(trndata['input'][i]))
    tarr=list()
    #np.ndarray(len(trndata['target'][i]))
    for t in range(len(trndata['input'][i])):
        arr.append([trndata['input'][i][t]])
    ndarr=np.asarray(arr)
    for t in range(len(trndata['target'][i])):
        tarr.append([trndata['target'][i][t]])
    ndtarr=np.asarray(tarr)
   # arr.reshape(9,1)
    training_data.append((ndarr,ndtarr))

for i in range(len(tstdata)):
    arr=list()
    #np.ndarray(len(trndata['input'][i]))
    tarr=list()
    #np.ndarray(len(trndata['target'][i]))
    for t in range(len(tstdata['input'][i])):
        arr.append([tstdata['input'][i][t]])
    ndarr=np.asarray(arr)
    #for t in range(len(tstdata['target'][i])):
    #    tarr.append([tstdata['target'][i][t]])
    #ndtarr=np.asarray(tarr)
   # arr.reshape(9,1)
    test_data.append((ndarr,tstdata['target'][i]))
stat=([1],[1],[1],[1])
k=0
while abs(stat[1][-1]-len(tstdata['input']))>1:
    tstdata,trndata  = alldata.splitWithProportion(0.15)
    trndata._convertToOneOfMany( )
    #net.large_weight_initializer()
    training_data=list()
    test_data=list()
    for i in range(len(trndata)):
        arr=list()
    #np.ndarray(len(trndata['input'][i]))
        tarr=list()
    #np.ndarray(len(trndata['target'][i]))
        for t in range(len(trndata['input'][i])):
            arr.append([trndata['input'][i][t]])
            ndarr=np.asarray(arr)
        for t in range(len(trndata['target'][i])):
            tarr.append([trndata['target'][i][t]])
        ndtarr=np.asarray(tarr)
   # arr.reshape(9,1)
        training_data.append((ndarr,ndtarr))

    for i in range(len(tstdata)):
        arr=list()
    #np.ndarray(len(trndata['input'][i]))
        tarr=list()
    #np.ndarray(len(trndata['target'][i]))
        for t in range(len(tstdata['input'][i])):
            arr.append([tstdata['input'][i][t]])
        ndarr=np.asarray(arr)
    #for t in range(len(tstdata['target'][i])):
    #    tarr.append([tstdata['target'][i][t]])
    #ndtarr=np.asarray(tarr)
   # arr.reshape(9,1)
        test_data.append((ndarr,tstdata['target'][i]))
#print 'cool'
    #training_data=list(trndata['input'][i],trndata['target'][i]) for i in trndata.length())
    #test_data=(tstdata['input'],tstdata['target'])
    #stat=net.SGD(training_data, 1000, 3, 0.07, lmbda = 1, evaluation_data=test_data,monitor_evaluation_accuracy=True, monitor_training_cost=True, monitor_training_accuracy=True)
    stat=net.SGD(training_data, 400, 3, 0.5, lmbda = 1, evaluation_data=test_data,monitor_evaluation_accuracy=True, monitor_training_cost=True, monitor_training_accuracy=True)
    nets_all=list()
    nets_all.append((net,stat))
    k=k+1
#net.SGD(training_data, 400, 10, 0.5, evaluation_data=test_data, monitor_evaluation_cost=True, monitor_evaluation_accuracy=True,monitor_training_cost=True, monitor_training_accuracy=True)
serial.serialise(nets_all,'nets_new_large_2_2')'''
print 'a'