# Tipo abstracto Grafo
# Javier Corbalan y Victor Soria
# 15 Marzo 2018

from Vertice import Vertice
from Arista import Arista
import heapq


# Clase que permite representar un grafo en memoria.
#   Esta compuesto por una lista de veritces y una lista de aristas

class Grafo:

    # Constructor de la clase grafo
    def __init__(self, num_vertices, num_aristas):
        self.num_vertices = num_vertices
        self.num_aristas = num_aristas
        self.vertices = []
        self.aristas = []
        self.ordenado = False
        self.max_ts = 0

        for i in range(0, num_vertices):
            vertice = Vertice(i)
            self.vertices.append(vertice)

    # Funcion que añade una arista al grafo. Internamente se representan como dos aristas dirigidas.
    def add_arista(self, vertice_inicial, vertice_final, timestamp):
        arista = Arista(vertice_inicial, vertice_final, timestamp)
        arista_invertida = Arista(vertice_final, vertice_inicial, timestamp)
        self.vertices[vertice_inicial].add_arista(arista)
        self.vertices[vertice_final].add_arista(arista_invertida)

        heapq.heappush(self.aristas,[timestamp, arista])
        # Actualiza el maximo timestamp si hace falta
        if self.max_ts < timestamp:
            self.max_ts = timestamp

    # Ordena el conjunto de las aristas por timestamp
    def ordenar(self):
        aux = []

        for i in range(0,self.num_aristas):
            timestamp, arista = heapq.heappop(self.aristas)
            aux.append(arista)

        self.aristas = aux
        self.ordenado = True

    # Obtiene la arista con el timestamp "indice", comenzando desde el menor timestamp.
    def get_arista(self, indice):
        if self.ordenado == False :
            self.ordenar()

        return self.aristas[indice]


    """
        Algoritmo recorre los vertices desde el primer infectado anyadiendo un nuevo infectado
        cada vez. Para ello utiliza la arista con menor timestamp que une un nodo infectado
        con otro que no lo esta. Para ello se utiliza un monticulo donde se anyaden todas
        las aristas de los nodos infectados.
        
        El coste del algoritmo:     (n es el numero de vertices)
            El coste en espacio en el caso peor es O(n**2). Ya que es necesario almacenar todos 
                los vertices(n), y el numero de aristas(n**2 en el caso peor)
            El coste en tiempo en el peor caso es O(n**3) en el caso en el que todas las aristas
                tengan el mismo timestamp. Ya que se recorren n vertices y para cada vertice se
                pueden sacar del orden de n**2 aristas.
            El coste en tiempo en el caso de que las aristas sean diferentes O(n**2 * log(n)),
                si necesario recorrer todos los vertices, y cada vertice posea n-1 aristas, 
                anyadir cada arista supone un coste (log n).
    """
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

            while arista_elegida == None and len(vector_aristas) > 0:

                timestamp, arista = heapq.heappop(vector_aristas) # O(log(n))

                if timestamp < time or arista.get_vertice_final() in conjunto_visitados:
                    continue        # O(n)

                arista_elegida = arista

            if arista_elegida is None:
                return False

            id_nuevo_vertice = arista_elegida.get_vertice_final()
            conjunto_visitados.append(id_nuevo_vertice)
            time = arista_elegida.get_timestamp()

            for arista in self.vertices[id_nuevo_vertice].get_aristas(): # O(n * log(n))
                if arista.timestamp < timestamp:
                    continue
                heapq.heappush(vector_aristas,[arista.get_timestamp(), arista]) # O(log(n))

        return arista_elegida.get_timestamp() <= query.get_timestamp_consulta()



    """
        Algoritmo que recorre las aristas ordenadas por timestamp menor a mayor. Utiliza un vector
        que almacena cuando un vector ha sido infectado. Los vertices que no han sido infectados
        tienen valor -1.
        
        El coste del algoritmo:     (n es el numero de vertices)
            El coste en espacio en el caso peor es O(n**2). Ya que es necesario almacenar todos 
                los vertices(n), y el numero de aristas(n**2 en el caso peor)
            El coste en tiempo en el peor caso es O(n**3), ya que en el caso de que todas las
                aristas tengan el mismo timestamp, el recorrido de los nodos infectados no es
                trivial(De menor timestamp a mayor). Por lo que tras infectar cada nuevo nodo
                es necesario comprobar de nuevo las aristas que anteriormente no han infectado
                a ningun nuevo nodo.
            El coste en tiempo en el caso de que cada arista tenga un timestamp diferente es
                O(n**2). Corresponde con recorrer todas las aristas una unica vez.
    """
    def do2(self, query):
        nodo_inicial = query.get_nodo_infectado()
        nodo_final = query.get_nodo_consulta()
        timestamp_infeccion = query.get_timestamp_infeccion()
        timestamp_consulta = query.get_timestamp_consulta()

        infectados = []
        for i in range(0, self.num_vertices):
            infectados.append(-1)

        infectados[nodo_inicial] = timestamp_infeccion

        espera = []
        modificado = False
        tamanyo = 0
        for i in range(0,self.num_aristas):
            arista = self.get_arista(i)

            if arista.timestamp < timestamp_infeccion:
                continue
            if arista.timestamp > timestamp_consulta:
                break

            if tamanyo > 0:
                if espera[0].timestamp < arista.timestamp:
                    if modificado:
                        self.eliminarEsperando(infectados, espera)
                        espera = []
                        modificado = False
                        tamanyo = 0
                    else:
                        espera = []
                        modificado = False
                        tamanyo = 0


            if infectados[arista.vertice_inicial] == -1 and infectados[arista.vertice_final] == -1:
                tamanyo = tamanyo + 1
                espera.append(arista)

            if infectados[arista.vertice_inicial] > -1 and infectados[arista.vertice_final] == -1:
                infectados[arista.vertice_final] = arista.timestamp
                if tamanyo > 0:
                    modificado = True

            if infectados[arista.vertice_inicial] == -1 and infectados[arista.vertice_final] > -1:
                infectados[arista.vertice_inicial] = arista.timestamp
                if tamanyo > 0:
                    modificado = True

        return (infectados[nodo_final] != -1) and (infectados[nodo_final] <= timestamp_consulta)


    """
        Funcion que recorre de forma recursiva la lista de aristas "espera". Esta lista contiene aristas
        con el mismo timestamp. Si algun nodo resulta infectado al recorrer la lista se vuelve a llamar recursivamente
        Sino finaliza su ejecucion
    """
    def eliminarEsperando(self, infectados, espera):
        pendientes = []
        tamanyo = 0
        modificado = False
        for arista in espera:
            if infectados[arista.vertice_inicial] == -1 and infectados[arista.vertice_final] == -1:
                tamanyo = tamanyo + 1
                pendientes.append(arista)

            if infectados[arista.vertice_inicial] > -1 and infectados[arista.vertice_final] == -1:
                infectados[arista.vertice_final] = arista.timestamp
                if tamanyo > 0:
                    modificado = True

            if infectados[arista.vertice_inicial] == -1 and infectados[arista.vertice_final] > -1:
                infectados[arista.vertice_inicial] = arista.timestamp
                if tamanyo > 0:
                    modificado = True

        if modificado:
            self.eliminarEsperando(infectados, pendientes)

    # Devuelve el mayor timestamp de las aristas del grafo
    def get_max_ts(self):
        return self.max_ts

    # Devuelve el numero de vertices del grafo
    def get_num_vertices(self):
        return self.num_vertices

    # Devuelve el numero de aristas del grafo
    def get_num_aristas(self):
        return self.num_aristas