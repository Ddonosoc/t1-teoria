from InvAFND import *
from ER2AFND import *
from tarea1 import *

e = []
for i in range(0, 11):
    e.append(estado(str(i)))

e[0].trans.append([e[1], ''])
e[0].trans.append([e[10], ''])
e[1].trans.append([e[2], ''])
e[1].trans.append([e[5], ''])
e[2].trans.append([e[3], 'a'])
e[3].trans.append([e[4], 'b'])
e[4].trans.append([e[9], ''])
e[9].trans.append([e[1], ''])
e[5].trans.append([e[6], 'a'])
e[6].trans.append([e[7], 'b'])
e[7].trans.append([e[8], 'a'])
e[8].trans.append([e[9], ''])
e[9].trans.append([e[10], ''])

e[10].final = 1

tarea1("archivo1", "*a")
