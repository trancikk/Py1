import serial
import numpy as np

net=serial.load('nets_new_large_2_3')
def calculate(row):
    ndarr=np.asarray(row)
    ndarr.resize(9,1)
    res= ((net[0][0].feedforward(ndarr)))
    res_str='Fail rate= %s; \n Success rate= %s;' % tuple(res)
    res_str=res_str.replace('[', '')
    res_str=res_str.replace(']', '')
    return res_str
    
    

"""#print net[0][0]
succ=serial.load('success_norm')
fail=serial.load('fail_norm')
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
test_norm1=(succ[2].getNormalGen())
print '\n'
test_norm2=(fail[2].getNormalGen())
print test_norm1
print test_norm2
ndarr1=np.asarray(test_norm1)
ndarr1.resize(9,1)
ndarr2=np.asarray(test_norm2)
ndarr2.resize(9,1)
print ndarr1
print ndarr2
#res=calculate(test_norm1[0])
res1=calculate(ndarr1)
res2=calculate(ndarr2)
#resa=net[0][0].accuracy([(list(test[8].getNormalGen()),1)])
#print res
#print '\n cool'
print res1
print succ[2].getResult();

print res2
print fail[2].getResult();
#import genini
#import gen
#print ['Keys- %s, value - %s;' % (genini.gens[i].getName(), genini.gens[i].getGens()) for i in genini.gens.keys()]
#print [i.printNormGens() for i in test]"""