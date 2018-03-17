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

        arista_elegida = None
        while( not (nodo_final in conjunto_visitados)):
            timestamp_minimo = float('Inf')
            arista_elegida = None

            for arista in vector_aristas:

                if arista.get_timestamp() < time or arista.get_vertice_final() in conjunto_visitados :
                    vector_aristas.remove(arista)
                    continue

                if arista.get_timestamp() < timestamp_minimo:
                    timestamp_minimo = arista.get_timestamp()
                    arista_elegida = arista

            if arista_elegida == None:
                return False

            id_nuevo_vertice = arista_elegida.get_vertice_final()
            conjunto_visitados.append(id_nuevo_vertice)
            time = arista_elegida.get_timestamp()

            nuevas_aristas = self.vertices[id_nuevo_vertice].get_aristas()
            vector_aristas = vector_aristas + nuevas_aristas

        return arista_elegida.get_timestamp() < query.get_timestamp_consulta()
