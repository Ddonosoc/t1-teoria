from ER2AFND import *
from AFND2AFD import *
from InvAFND import *


def tarea1(archivo, expresion):
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    automata = ER2AFND(expresion)
    texto = open(archivo + ".txt", 'r')
    print(texto.read())
    texto.close()


    #ARREGLAR ESTO
    automataMod = automata
    automatadet = AFND2AFD(automataMod, alfabeto)
    automatainv = InvAFND(automata)
