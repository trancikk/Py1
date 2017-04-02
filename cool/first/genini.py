# -*- coding: utf-8 -*-
import gen
import execution
print execution.head
import serial

gens=dict()
il8=gen.Gen(execution.head[0],'C','T')
gens.update(il8.getDict())
il10_592=gen.Gen(execution.head[1],'C','A')
gens.update(il10_592.getDict())
il10_1082=gen.Gen(execution.head[2],'G','A')
gens.update(il10_1082.getDict())
#print il8.getName()
#print il8.getGens()
print gens
#print gen.Gen.getGens(il8)
#print gen.Gens.getGen(execution.head[0])
serial.serialise(gens,'gens_dict')