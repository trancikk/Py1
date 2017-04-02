import serial
import person
import genini
import gen


data_gens=serial.load('gens_dict')
data_personf=serial.load('fail_norm')
data_persons=serial.load('success_norm')
for i in data_personf:
    print sorted(data_gens.keys())
    print i.getNormalGen()
    print i.getRow()

#for i in data_person:
 #   print sorted(i.getRow().keys())
    #for t in i.getRow().keys():
        #print data_gens[t]
        #print i.getRow()[t]
  #  i.setRow([data_gens[t].normalise(t,i.getRow()[t]) for t in sorted(i.getRow().keys())])
        #print data_gens[t].normalise(t,i.getRow()[t])
   # print i.gens_normalise
    #print i.printGens()