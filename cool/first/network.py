# -*- coding: utf-8 -*-
from pybrain.structure import FeedForwardNetwork
import serial
from pybrain.datasets import SupervisedDataSet
import person
#TODO ?
n = FeedForwardNetwork()
dssuccess=serial.load('success_norm')
dsfail=serial.load('fail_norm')
head=serial.load('gens')
full=dsfail+dssuccess
#print len(dssuccess)
#print len(full)
t=0
for i in (full):
    print t
    i.printGens()
    print 'kkkeys -%s'%i.getProp().keys()
    print i.getSurname()
    print i.getResult()
    t+=1
#ds=SupervisedDataSet(9,1)
#ds.addSample(inp, target)
from pybrain.structure import LinearLayer, SigmoidLayer
inLayer = LinearLayer(2, name='in')
hiddenLayer = SigmoidLayer(3, name='hide')
outLayer = LinearLayer(1, name='out')
n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)
from pybrain.structure import FullConnection
in_to_hidden = FullConnection(inLayer, hiddenLayer, name = 'con1')
hidden_to_out = FullConnection(hiddenLayer, outLayer, name='con2')
n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)
n.sortModules()
print n
serial.serialise(n,'network')
print 'good'
netw=serial.load('network')
print netw