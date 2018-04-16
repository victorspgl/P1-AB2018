# Programa Principal. Lectura de ficheros y querys
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

import cProfile
from random_graph import random_graph
from description_file_reader import read_description
from Query import Query


########################################################################################################################
#############################         Funciones de entrada de comandos         #########################################
########################################################################################################################

def muestra_ayuda():
    print(" El comando 'c' permite cambiar fichero de referencia")
    print(" Este fichero debe seguir el siguiente formato:")
    # TODO: Especificar formato de los ficheros de entradaa
    print(" El comando 'q' permite introducir una query al sistema")
    print(" La query debe tener el siguiente formato:")
    # TODO: Especificar el forma de las querys


""" Funcion que pide al usuario el nombre de un fichero y lo intenta interpretar. Si el fichero no es valido lo vuelve
    a intentar. """


def leer_nombre_fichero():
    correcto = False
    while not correcto:
        nombre_fichero = raw_input("Introduce fichero de entrada: ")

        try:
            configuracion = read_description(nombre_fichero)
            correcto = True
        except:
            print("Fichero en formato incorrecto o ilegible")

    return configuracion


""" Funcion que pide al usuario una query. Si la query no es valida lo vuelve a intentar. """


def leer_query():
    correcto = False
    while not correcto:
        lectura_teclado = raw_input("Introduce query: ")

        try:
            query = Query(lectura_teclado)
            correcto = True
        except:
            print("Query en formato incorrecto")

    return query


""" Funcion que pide al usuario la descripcion del grafo. Si la descripcion no es valida lo vuelve a intentar. """


def leer_descripcion():
    correcto = False
    while not correcto:
        string = raw_input("Introduce numero de vertices, aristas y el tiempo de comunicacion maximo: ")

        try:
            num_vertices, num_aristas, max_timestamp = [int(i) for i in string.split(' ')]
        except:
            print("Descripcion en formato incorrecto")
            continue

        try:
            random_graph(num_vertices, num_aristas, max_timestamp)
        except:
            print("Error al crear el fichero")
            continue

        try:
            configuracion = read_description("random_graph.txt")
            correcto = True
        except:
            print("Error al cargar el fichero")

    return configuracion


########################################################################################################################
##########################################         MAIN         ########################################################
########################################################################################################################

configuracion = leer_nombre_fichero()

print("Introduce un comando:")
print("c - cambiar fichero de referencia")
print("q - realizar una query")
print("v - visualizar el fichero de referencia")
print("r - crear un grafo aleatorio y cargarlo en memoria")
print("h - ayuda")

while True:

    comando = raw_input("$$: ")

    if (comando == "c"):
        configuracion = leer_nombre_fichero()
    elif (comando == "q"):
        query = leer_query()
        cProfile.run('configuracion.do(query)')
        infectado = configuracion.do(query)
        if infectado:
            print("Nodo infectado")
        else:
            print("Nodo no infectado")
    elif (comando == "h"):
        muestra_ayuda()
    elif (comando == "v"):
        configuracion.dibujar()
    elif (comando == "r"):
        configuracion = leer_descripcion()
    else:
        print("Comando incorrecto")
        muestra_ayuda()

    print("Introduce un comando:")
