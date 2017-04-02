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

il6_174=gen.Gen(execution.head[3],'G','C')
gens.update(il6_174.getDict())

fvii_1097=gen.Gen(execution.head[4],'G','A')
gens.update(fvii_1097.getDict())

gp1a_807=gen.Gen(execution.head[5],'C','T')
gens.update(gp1a_807.getDict())

fii_2021=gen.Gen(execution.head[6],'G','A')
gens.update(fii_2021.getDict())

fv_1691=gen.Gen(execution.head[7],'G','A')
gens.update(fv_1691.getDict())

mtrhfr_677=gen.Gen(execution.head[8],'C','T')
gens.update(mtrhfr_677.getDict())
#print il8.getName()
#print il8.getGens()
#print gens
#print gen.Gen.getGens(il8)
#print gen.Gens.getGen(execution.head[0])
serial.serialise(gens,'gens_dict')