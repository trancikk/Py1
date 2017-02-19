from pybrain.structure import FeedForwardNetwork
n = FeedForwardNetwork()
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
<<<<<<< Upstream, based on origin/first
print n
=======
print(n)
>>>>>>> 36d6677 
n.activate([1, 2])
print(in_to_hidden.params)
print(hidden_to_out.params)
print(n.params)
print('good')