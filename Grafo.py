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
        arista_invertida = Arista(vertice_final, vertice_inicial, timestamp)
        self.vertices[vertice_inicial].add_arista(arista)
        self.vertices[vertice_final].add_arista(arista_invertida)

    def do(self,query):
        nodo_inicial = query.get_nodo_infectado()
        nodo_final = query.get_nodo_consulta()
        conjunto_visitados = [nodo_inicial]
        vector_aristas = self.vertices[nodo_inicial].get_aristas()
        time = query.get_timestamp_infeccion()

        while( not (nodo_final in conjunto_visitados)):
            timestamp_minimo = float('Inf')
            arista_elegida = None

            for arista in vector_aristas:

                if arista.get_timestamp() < time :
                    vector_aristas.remove(arista)
                    continue

                if arista.get_timestamp() < timestamp_minimo:
                    timestamp_minimo = arista.get_timestamp
                    arista_elegida = arista

            conjunto_visitados.append(arista_elegida.get_vertice_final())


