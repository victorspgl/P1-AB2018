# Tipo abstracto Grafo
# Javier Corbalan y Victor Soria
# 15 Marzo 2018

from Vertice import Vertice
from Arista import Arista
import heapq
import networkx as nx

class Grafo:
    def __init__(self, num_vertices, num_aristas):
        self.num_vertices = num_vertices
        self.num_aristas = num_aristas
        self.vertices = []
        self.aristas = []
        self.ordenado = False

        for i in range(0, num_vertices):
            vertice = Vertice(i)
            self.vertices.append(vertice)

    def add_arista(self, vertice_inicial, vertice_final, timestamp):
        arista = Arista(vertice_inicial, vertice_final, timestamp)
        arista_invertida = Arista(vertice_final, vertice_inicial, timestamp)
        self.vertices[vertice_inicial].add_arista(arista)
        self.vertices[vertice_final].add_arista(arista_invertida)

        heapq.heappush(self.aristas,[timestamp, arista])

    def ordenar(self):
        aux = []

        for i in range(0,self.num_aristas):
            aux.append(heapq.heapop())

        self.aristas = aux


    def get_arista(self, indice):
        if self.ordenado == False :
            self.ordenar()

        return self.aristas[indice]


    def dibujar(self):
        G = nx.Graph()
        G.add_nodes_from(range(0, self.num_vertices))
        for vert in self.vertices:
            for aris in vert.get_aristas():
                G.add_edge(vert.id, aris.get_vertice_final(), weight=aris.get_timestamp())

        edge_labels = dict([((u, v,), d['weight'])
                            for u, v, d in G.edges(data=True)])
        pos = nx.spring_layout(G)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw_networkx(G, pos, node_size=1500, node_color='yellow')
        plt.show()

    def do(self, query):
        nodo_inicial = query.get_nodo_infectado()
        nodo_final = query.get_nodo_consulta()
        if nodo_inicial == nodo_final:
            if query.get_timestamp_consulta() >= query.get_timestamp_infeccion():
                return True
            else:
                return False

        conjunto_visitados = [nodo_inicial]
        vector_aristas = []
        for arista in self.vertices[nodo_inicial].get_aristas():
            heapq.heappush(vector_aristas,[arista.get_timestamp(), arista])
        time = query.get_timestamp_infeccion()

        while (not (nodo_final in conjunto_visitados)):
            arista_elegida = None

            while arista_elegida == None:

                timestamp, arista = heapq.heappop(vector_aristas)

                if timestamp < time or arista.get_vertice_final() in conjunto_visitados:
                    continue

                arista_elegida = arista

            if arista_elegida is None:
                return False

            id_nuevo_vertice = arista_elegida.get_vertice_final()
            conjunto_visitados.append(id_nuevo_vertice)
            time = arista_elegida.get_timestamp()

            for arista in self.vertices[id_nuevo_vertice].get_aristas():
                heapq.heappush(vector_aristas,[arista.get_timestamp(), arista])

        return arista_elegida.get_timestamp() <= query.get_timestamp_consulta()


    def do2(self, query):
        nodo_inicial = query.get_nodo_infectado()
        nodo_final = query.get_nodo_consulta()
        time = query.get_timestamp_infeccion()
        limite = query.get_timestamp_consulta()

        if nodo_inicial == nodo_final:
            if query.get_timestamp_consulta() >= query.get_timestamp_infeccion():
                return True
            else:
                return False

        vector_nodos = []
        heapq.heappush(vector_nodos,[time, nodo_inicial])
        nodos_visitados = []

        while True:

            timestamp, nodo_siguiente = heapq.heappop(vector_nodos)

            if nodo_siguiente == nodo_final:
                return timestamp >= query.get_timestamp_consulta()

            lista_aristas = self.vertices[nodo_siguiente].get_aristas()

            for arista in lista_aristas:
                if  (arista.get_timestamp() >= timestamp and arista.get_timestamp() < limite):
                    heapq.heappush(vector_nodos,[arista.timestamp, arista.get_vertice_final()])