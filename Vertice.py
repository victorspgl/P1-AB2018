# Tipo abstracto Vertice
# Javier Corbalan y Victor Soria
# 15 Marzo 2018

class Vertice:

    def __index__(self, id):
        self.id = id
        self.aristas = []

    def add_arista(self,arista):
        self.aristas.append(arista)

    def get_aristas(self):
        return self.aristas