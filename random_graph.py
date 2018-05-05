# Modulo de generacion de grafo aleatorio en fichero txt.
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

import random
from Grafo import Grafo
import numpy as np

def random_graph(conFichero, num_vertices, num_aristas, max_time):
    if num_aristas > num_vertices*(num_vertices -1):
        print("Numero de aristas superior a n*(n-1). Siendo n el numero de vertices.")
        raise Exception

    if conFichero:
        fichero_objeto = open("random_graph.txt", "w")
        fichero_objeto.write(str(num_vertices) + " " + str(num_aristas) + "\n")

    configuracion = Grafo(num_vertices, num_aristas)

    matriz_conectados = []
    for i in range(0,num_vertices):
        matriz_conectados.append(range(0, num_vertices))
        matriz_conectados[i].pop(i)

    for i in range(0,num_aristas):
        nok = True
        while nok:
            vertice_inicial = random.randint(0, num_vertices - 1)
            vertice_final = random.randint(0, num_vertices - 1)
            try:
                vertice_final = matriz_conectados[vertice_inicial].pop(vertice_final)
                nok = False
            except:
                nok = True

        timestamp = random.randint(1, max_time)

        configuracion.add_arista(vertice_inicial, vertice_final, timestamp)

    configuracion.ordenar()

    if conFichero:
        for i in range(0,num_aristas):

            arista = configuracion.get_arista(i)

            vertice_inicial = arista.get_vertice_inicial()
            vertice_final = arista.get_vertice_final()
            timestamp = arista.get_timestamp()

            fichero_objeto.write(str(vertice_inicial) + " ")
            fichero_objeto.write(str(vertice_final) + " ")
            fichero_objeto.write(str(timestamp))
            fichero_objeto.write("\n")
        fichero_objeto.close()

    return configuracion

