# Tipo abstracto Vertice
# Javier Corbalan y Victor Soria
# 15 Marzo 2018

# Clase que representa un vertice de un grafo. Esta esta compuesta por un identificador y una lista de aristas dirigidas
#   que parten de ese vertice.

class Vertice:
    def __init__(self, id):
        self.id = id
        self.aristas = []

    def add_arista(self, arista):
        self.aristas.append(arista)

    def get_aristas(self):
        return self.aristas
