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
tstdata, trndata = alldata.splitWithProportion( 0.25 )
print "Number of training patterns: ", len(trndata)
print "Input and output dimensions: ", trndata.indim, trndata.outdim
print "First sample (input, target, class):"
#print trndata['input'][0], trndata['target'][0], trndata['class'][0]

inLayer = LinearLayer(9, name='in')
hiddenLayer = SigmoidLayer(9, name='hide')
outLayer = LinearLayer(1, name='out')
n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

in_to_hidden = FullConnection(inLayer, hiddenLayer, name = 'con1')
hidden_to_out = FullConnection(hiddenLayer, outLayer, name='con2')
n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)

fnn = buildNetwork( trndata.indim, 5, trndata.outdim, outclass=SoftmaxLayer )
trainer = BackpropTrainer( fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)
for i in range(10):
    trainer.trainEpochs(10)
print fnn.activate(tstdata['input'][0])
print tstdata['target'][0]
print fnn.activate(trndata['input'][1])
print trndata['target'][1]
n.sortModules()
print n
serial.serialise(n,'network')
print 'good'
netw=serial.load('network')
print netw