from estado import *


# Funcion que permite obtener el arbol a partir de la expresion regular, para generar el automata
def readnext(ER):
    first = ER[0]
    simbolos = "|*.()"


# Funcion que inicializa las variables para luego llamar a la funcion "recursiva" y construir el automata
def ER2AFND(ER):
    inicial = estado(1)
    final = estado(1)
    automata = []
    automata.append(inicial)
    automata.append(final)
    ER2AFNDI(ER, automata, 0, 1)


# Funcion recursiva que construye el automata segun los simbolos utilizados
def ER2AFNDI(ER, auto, i, j):
    simbolos = readnext(ER)
    if simbolos[0] == '*':
        estado1 = estado(i+1)
        estado2 = estado(i+2)
        auto.append(estado1)
        auto.append(estado2)
        auto[i].trans.append([i+1, ''])
        auto[i+2].trans.append([j, ''])
        auto[i+2].trans.append([i+1, ''])
        ER2AFNDI(simbolos[1], auto, i+1, i+2)
