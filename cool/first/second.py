from pybrain.structure import RecurrentNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
n = RecurrentNetwork()
n.addInputModule(LinearLayer(2, name='in'))
n.addModule(SigmoidLayer(3, name='hidden'))
n.addOutputModule(LinearLayer(1, name='out'))
n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))
n.addRecurrentConnection(FullConnection(n['hidden'], n['hidden'], name='c3'))
n.sortModules()
print(n.activate((2, 2)))
print(n.activate((2, 2)))
print(n.activate((2, 2)))
n.reset()
print(n.activate((2, 2)))