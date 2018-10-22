
# Clase que contiene los estados para construir el automata
class estado:
    def __init__(self, index):
        self.id = index
        self.trans = []
        self.final = 0
