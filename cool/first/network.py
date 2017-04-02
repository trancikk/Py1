# -*- coding: utf-8 -*-
from pybrain.structure import FeedForwardNetwork
import serial
from pybrain.datasets import SupervisedDataSet
import person
from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal
import numpy
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
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

inLayer = LinearLayer(9, name='in')
hiddenLayer = SigmoidLayer(3, name='hide')
outLayer = LinearLayer(1, name='out')
n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

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