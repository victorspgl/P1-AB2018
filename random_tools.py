# Modulo de generacion de grafo aleatorio en fichero txt.
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

import random
from Grafo import Grafo

"""
    Funcion que genera un grafo aleatorio. Donde no existe mas de una arista entre dos vertices.
"""
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

"""
    Funcion que genera un fichero que contiene "n" queries.
"""
def n_queries_aleatorios(configuracion, n):
    fichero_objeto = open("random_queries.txt", "w")
    fichero_objeto.write(str(n) + "\n")
    for i in range(0, n):
        max_vert = configuracion.get_num_vertices()
        max_ts = configuracion.get_max_ts()

        nodo_infectado = random.randrange(0, max_vert)
        fichero_objeto.write(str(nodo_infectado) + " ")

        ts_infeccion = random.randrange(0, max_ts)
        fichero_objeto.write(str(ts_infeccion) + " ")

        nodo_consulta = random.randrange(0, max_vert)
        fichero_objeto.write(str(nodo_consulta) + " ")

        ts_consulta = random.randrange(ts_infeccion, max_ts)
        fichero_objeto.write(str(ts_consulta))
        fichero_objeto.write("\n")
    fichero_objeto.close()
