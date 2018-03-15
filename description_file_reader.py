# Lector de ficheros de descripcion del grafo
# Javier Corbalan y Victor Soria
# 15 Marzo 2018

from Grafo import Grafo


#
# Lee un fichero de descripcion que contiene en la primera fila el numero de vertices y de aristas separados por un
#   espacio. A continuacion el fichero describe cada arista. Vertice inicial, vertice final, y timestamp asociado a la
#   arista.
#

def read_description(nombreFichero):
    fichero_objeto = open(nombreFichero, "r")
    lineas = fichero_objeto.readlines()
    num_vertices, num_aristas = [int(i) for i in lineas[0].split(' ')]

    configuracion = Grafo(num_vertices, num_aristas)

    for linea in range(1, num_aristas):
        vertice_inicio, vertice_fin, timestamp = [int(i) for i in lineas[linea].split(' ')]
        configuracion.add_arista(vertice_inicio, vertice_fin, timestamp)

    return configuracion
