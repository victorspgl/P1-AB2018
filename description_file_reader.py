# Lector de ficheros de descripcion del grafo
# Javier Corbalan y Victor Soria
# 15 Marzo 2018

from Grafo import Grafo
from Query import Query

#
# Lee un fichero de descripcion que contiene en la primera fila el numero de vertices y de aristas separados por un
#   espacio. A continuacion el fichero describe cada arista. Vertice inicial, vertice final, y timestamp asociado a la
#   arista.
#

def read_description_graph(nombre_fichero):
    fichero_objeto = open(nombre_fichero, "r")
    lineas = fichero_objeto.readlines()
    num_vertices, num_aristas = [int(i) for i in lineas[0].split(' ')]

    configuracion = Grafo(num_vertices, num_aristas)

    for linea in range(1, num_aristas + 1):
        vertice_inicio, vertice_fin, timestamp = [int(i) for i in lineas[linea].split(' ')]
        configuracion.add_arista(vertice_inicio, vertice_fin, timestamp)

    return configuracion

#
# Lee un fichero de descripcion que contiene en la primera fila el numero de queries almacenadas.
#   A continuacion el fichero describe cada query. Vertice infectado inicial, timestamp de infeccion, vertice consultado,
#   y timestamp consulta
#

def read_description_queries(nombre_fichero):
    fichero_objeto = open(nombre_fichero, "r")
    lineas = fichero_objeto.readlines()
    num_queries = [int(i) for i in lineas[0].split(' ')]

    queries = []
    for linea in range(1, num_queries[0] + 1):
        query = Query(lineas[linea])
        queries.append(query)
    return queries