# Modulo de generacion de grafo aleatorio en fichero txt.
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

import random

def random_graph(num_vertices, num_aristas, max_time):
    fichero_objeto = open("random_graph.txt", "w")
    fichero_objeto.write(str(num_vertices) + " " + str(num_aristas) + "\n")

    for i in range(0,num_aristas):
        vertice_inicial = random.randint(1, num_vertices)
        vertice_final = vertice_inicial
        while(vertice_final == vertice_inicial):
            vertice_final = random.randint(1, num_vertices)
        timestamp = random.randint(1, max_time)
        fichero_objeto.write(str(vertice_inicial) + " ")
        fichero_objeto.write(str(vertice_final) + " ")
        fichero_objeto.write(timestamp)
        fichero_objeto.write("\n")

    fichero_objeto.close()

