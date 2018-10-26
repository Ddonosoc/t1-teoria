from estado import *
from AFND2AFD import *
import copy


def InvAFND(automata):
    copyaut = copy.deepcopy(automata)
    auxiliar = []
    for i in range(0, len(copyaut)):
        auxiliar.append([])
    for i in range(0, len(copyaut)):
        if copyaut[i].final == 1 and copyaut[i].inicial == 0:
            copyaut[i].final = 0
            copyaut[i].inicial = 1
        elif copyaut[i].inicial == 1 and copyaut[i].final == 0:
            copyaut[i].final = 1
            copyaut[i].inicial = 0

        while len(copyaut[i].trans) >= 1:
            transb = copyaut[i].trans.pop()
            indice = buscar(transb[0], copyaut)
            if indice >= 0:
                tuplaN = [copyaut[i], transb[1]]
                auxiliar[indice].append(tuplaN)

    for i in range(0, len(copyaut)):
        copyaut[i].trans = auxiliar[i]
    return copyaut

