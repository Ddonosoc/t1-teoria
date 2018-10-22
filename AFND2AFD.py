from estado import *


# Funcion que convierte de AFND a AFD usando el algoritmo visto en clases
def AFND2AFD(automata, alfabeto):
    # Se toma la clausura epsilon del estado inicial
    inicial = ClausuraF(automata[0], '')
    inicial.append(automata[0])
    # Se crea un estado con nombre
    inicialAFD = estado(nombrar(inicial))
    inicialAFD.final = hayFinal(inicial)
    # Lista de estados pendientes (por revisar)
    pendientes = []
    pendientes.append(inicial)
    # creacion del AFD con estado inicial
    AFD = []
    AFD.append(inicialAFD)
    # Mientras hayan elementos en el arreglo pendientes
    visitados = []
    while pendientes:
        anterior = pendientes.pop()
        visitados.append(anterior)
        for simbolo in alfabeto:
            estados = []
            for pend in anterior:
                # ver la clausura de los estados pendientes
                arreglo = ClausuraF(pend, simbolo)
                if arreglo:
                    for elem in arreglo:
                        if elem not in estados:
                            estados.append(elem)
            if estados:
                # Si hay elementos en la lista de estados objetivos, se agregan como transicion dependiendo de si los
                # estados existen o no
                if estados not in pendientes and estados != anterior and estados not in visitados:
                    pendientes.append(estados)
                hayFinalSig = hayFinal(estados)
                estadoAFD = estado(nombrar(anterior))
                estadoAFDsig = estado(nombrar(estados))
                indice = buscar(estadoAFD, AFD)
                indiceSig = buscar(estadoAFDsig, AFD)
                estadoAFDsig.final = hayFinalSig
                if indiceSig >= 0 and indice >= 0:
                    tupla = [AFD[indiceSig], simbolo]
                    AFD[indiceSig].final = hayFinalSig
                    if tupla not in AFD[indice].trans:
                        AFD[indice].trans.append(tupla)
                elif indiceSig >= 0 and indice < 0:
                    AFD[indiceSig].final = hayFinalSig
                    estadoAFD.trans.append([AFD[indiceSig], simbolo])
                    AFD.append(estadoAFD)
                elif indiceSig < 0 and indice < 0:
                    estadoAFD.trans.append([estadoAFDsig, simbolo])
                    AFD.append(estadoAFD)
                    AFD.append(estadoAFDsig)
                elif indiceSig < 0 and indice >= 0:
                    tupla = [estadoAFDsig, simbolo]
                    if tupla not in AFD[indice].trans:
                        AFD[indice].trans.append(tupla)
                    AFD.append(estadoAFDsig)
    return AFD


# Funcion que permite crear un estado a partir de un arreglo de estado, usando sus identificaciones
def nombrar(arreglo):
    nombre = ''
    for estados in arreglo:
        nombre += estados.id
    return nombre


# Funcion que permite comparar si las dos id de dos estados son iguales
def iguales(nombre1, nombre2):
    if len(nombre1) != len(nombre2):
        return 0
    else:
        for i in range(0, len(nombre1)):
            if nombre1[i] not in nombre2 or nombre2[i] not in nombre1:
                return 0
        return 1


def hayFinal(arreglo):
    for est in arreglo:
        if est.final == 1:
            return 1
    return 0


# Funcion que busca si en un arreglo esta el estado dado, entrega el indice del arreglo en donde esta ubicado
def buscar(estadoI, arreglo):
    resultado = -1
    for i in range(0, len(arreglo)):
        if iguales(estadoI.id, arreglo[i].id):
            resultado = i
            break
    return resultado

# Funcion que busca algun camino desde cierto estado usando como simbolo solo epsilon o el simbolo dado
# Retorna un arreglo de estados que cumplen lo anterior
def Clausura(estadoI, simbolo, consumido, visitados, final):
    if estadoI not in visitados:
        visitados.append(estadoI)
        for trans in estadoI.trans:
            if trans[1] == simbolo and not consumido:
                final.append(trans[0])
                Clausura(trans[0], simbolo, 1, visitados, final)
            elif trans[1] == '' and not consumido:
                Clausura(trans[0], simbolo, consumido, visitados, final)
            elif trans[1] == '' and consumido:
                final.append(trans[0])
                Clausura(trans[0], simbolo, consumido, visitados, final)

# Funcion que inicializa los objetos y retorna la lista que modifica Clausura
def ClausuraF(estadoI, simbolo):
    final = []
    visitados = []
    consumido = 0
    Clausura(estadoI, simbolo, consumido, visitados, final)
    return final


# Funcion que encuentra el estado x en el automata
def find(automata, estado):
    result = []
    for elem in automata:
        if elem == estado:
            result = elem
            break
    return result


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
    print(elem.id, elem.final)

