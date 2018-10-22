from estado import *
from AFND2AFD import *


def InvAFND(automata):
    copyAutomata = automata.copy()
    for i in range(0, len(automata)):
        if automata[i].final == 1:
            automata[0].final = 0
        if i == 0:
            automata[0].final = 1
        for trans in automata[i].trans:
            indice = buscar(trans[0], automata)
            if indice >= 0:
                trans[0] = automata[i]
                automata[indice].trans.append(trans)
                automata[i].trans.remove(trans)
    return copyAutomata


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

afd = AFND2AFD(e, 'ab')
for elem in afd:
    print("")
    print("Estado ", elem.id)
    print("=== Transiciones ===")
    for trans in elem.trans:
        print(trans[0].id, trans[1])

print("======== Invertido =========")
afdInv = InvAFND(afd)
for elem in afdInv:
    print("")
    print("Estado ", elem.id)
    print("=== Transiciones ===")
    for trans in elem.trans:
        print(trans[0].id, trans[1])
