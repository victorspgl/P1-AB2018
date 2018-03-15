# Tipo abstracto Grafo
# Javier Corbalan y Victor Soria
# 15 Marzo 2018

from Vertice import Vertice
from Arista import Arista


class Grafo:

    def __init__(self, num_vertices, num_aristas):
        self.num_vertices = num_vertices
        self.num_aristas  = num_aristas
        self.vertices = []

        for i in range(0,num_vertices):
            vertice = Vertice(i)
            self.vertices.append(vertice)

    def add_arista(self,vertice_inicial, vertice_final, timestamp):
        arista = Arista(vertice_inicial, vertice_final, timestamp)
        self.vertices[vertice_inicial].add_arista(arista)
        self.vertices[vertice_final].add_arista(arista)