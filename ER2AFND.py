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
    ER2AFNDI(ER, automata, inicial, final)


# Funcion recursiva que construye el automata segun los simbolos utilizados
# edit: ahora se trabaja sobre los estados y no sobre los indices del automata dado que los estados pueden tener
# indices duplicado dada la construcción
def ER2AFNDI(ER, auto, ini, fin):
    simbolos = readnext(ER)
    if simbolos[0] == '*':
        estado1 = estado(ini.id + 1)
        estado2 = estado(ini.id + 2)
        ini.trans.append([estado1, ''])
        estado2.trans.append([fin, ''])
        estado2.trans.append([estado1, ''])
        ini.trans.append([fin, ''])
        auto.append(estado1)
        auto.append(estado2)
        ER2AFNDI(simbolos[1], auto, estado1, estado2)
