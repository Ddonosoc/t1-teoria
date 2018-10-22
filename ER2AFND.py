from estado import *

EPSILON = "#"  # Constante (vacio)

# Determina si s es una expresion o parte del alfabeto
def isAlphaValid(s):
    # RegExp
    if (len(s)>1):
        return True
    # Un solo caracter
    return s.isalnum() or s == ' '

# Determina si s es un operador binario
def isOperator(s):
    return s == '.' or s == '|'

# Funcion que permite obtener el arbol a partir de la expresion regular, para generar el automata
def readNext(ER):
    pila = []
    s = 0
    # Mientras quede por leer, o no se haya llegado una sola operacion en la pila
    while s < len(ER) or len(pila) > 3:
        # Cuando termino de leer la ER
        if s == len(ER):
            op2 = pila.pop()
            op1 = pila.pop()
            # Caso de * (operador unario)
            if pila[0] == '*' and len(pila) != 2:
                pila.append([op1, op2])
            # Caso de |. (operadores binarios)
            else:
                pila.append([pila.pop(),op1,op2])

        # Cuando recibe cualquier operador
        elif isOperator(ER[s]) or ER[s]=='*':
            pila.append(ER[s])

        # Cuando recibe una ER/letra, pero la operacion es binaria
        elif isAlphaValid(ER[s]) and isOperator(pila[len(pila) - 1]):
            pila.append(ER[s])

        # Cuando recibe una ER/letra y la operacion es unaria
        elif isAlphaValid(ER[s]) and pila[len(pila)-1] == '*':
            pila.append([pila.pop(),ER[s]])

        # Cuando recibe una ER/letra, hay otra en el tope, y operacion es binaria
        elif isAlphaValid(ER[s]) and isAlphaValid(pila[len(pila)-1]):
            operand = pila.pop()
            pila.append([pila.pop(),operand, ER[s]])
        # Error? input invalido
        else:
            print("WTF")
        s += 1
    return pila


# Funcion que inicializa las variables para luego llamar a la funcion "recursiva" y construir el automata
def ER2AFND(ER):
    inicial = estado(0)
    final = estado('F')
    final.final = 1
    automata = []
    automata.append(inicial)
    automata.append(final)
    ER2AFNDI(readNext(ER), automata, inicial, final)
    imprimirAuto(automata)

# Lindo print para ver los automatas (debug only)
def imprimirAuto(auto):
    c = 0
    for estado in auto:
        #print(estado.trans)
        for transiciones in estado.trans:
            c += 1
            print(estado.id,"-",transiciones[1],"->",transiciones[0].id)
    print("Tiene ",len(auto), " estados y ",c," transiciones")

# Entrega el indice que identificara el siguiente estado a crear
def nextIndex(auto):
    return len(auto)-1

# Funcion recursiva que construye el automata segun los simbolos utilizados
# edit: ahora se trabaja sobre los estados y no sobre los indices del automata dado que los estados pueden tener
# indices duplicado dada la construcción
def ER2AFNDI(ER, auto, ini, fin):

    if len(ER) == 0: return
    first = ER[0]

    # Kleene
    if first[0] == '*':
        estado1 = estado(nextIndex(auto))
        estado2 = estado(nextIndex(auto)+1)
        ER2AFNDI(first[1:], auto, estado1, estado2)
        ini.trans.append([estado1, EPSILON])
        estado2.trans.append([fin, EPSILON])
        estado2.trans.append([estado1, EPSILON])
        ini.trans.append([fin, EPSILON])
        auto.append(estado1)
        auto.append(estado2)
        ER2AFNDI(ER[1:], auto, estado1, estado2)

    # ER/letras
    elif isAlphaValid(first[0]):
        ini.trans.append([fin,first[0]])

    # Concatenacion
    elif first[0] == '.':
        estado1 = estado(nextIndex(auto))
        auto.append(estado1)
        ER2AFNDI(first[1:],auto,ini,estado1)
        ER2AFNDI(first[2:],auto,estado1,fin)

    # Union
    elif first[0] == '|':
        estado1 = estado(nextIndex(auto))
        estado2 = estado(nextIndex(auto) + 1)
        auto.append(estado1)
        auto.append(estado2)
        ER2AFNDI(first[1:], auto, estado1, estado2)
        estado3 = estado(nextIndex(auto))
        estado4 = estado(nextIndex(auto)+1)
        auto.append(estado3)
        auto.append(estado4)
        ER2AFNDI(first[2:], auto, estado3, estado4)
        ini.trans.append([estado1, EPSILON])
        ini.trans.append([estado3, EPSILON])
        estado2.trans.append([fin, EPSILON])
        estado4.trans.append([fin, EPSILON])
