# Programa Principal. Lectura de ficheros y querys
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

import cProfile
from random_graph import random_graph
from description_file_reader import read_description
from Query import Query
import random


########################################################################################################################
#############################         Funciones de entrada de comandos         #########################################
########################################################################################################################

def muestra_ayuda():
    print(" El comando 'c' permite cambiar fichero de referencia")
    print(" Este fichero debe seguir el siguiente formato:")
    print("     En la primera linea figura el numero de vertices y el numero de aristas, ambas cifras separadas por un espacio")
    print("     En las siguientes lineas se describen las aristas usando el formato vertice_inicio, vertice_fin, timestamp")
    print(" El comando 'q' permite introducir una query al sistema, utiliza el metodo 1")
    print(" El comando 'q' permite introducir una query al sistema, utiliza el metodo 2")
    print(" El comando 'r' permite crear un grafo aleatorio, especificandolo de la siguiente manera:")
    print(" El comando 'rf' permite crear un grafo aleatorio y guardarlo en un fichero")
    print(" La query debe tener el siguiente formato:")
    print("     nodo comienzo infeccion, timestamp de infeccion, nodo a consultar, timestamp de la consulta")

""" Funcion que pide al usuario el nombre de un fichero y lo intenta interpretar. Si el fichero no es valido lo vuelve
    a intentar. """


def leer_nombre_fichero():
    configuracion = None
    while configuracion is None:
        nombre_fichero = raw_input("Introduce fichero de entrada: ")
        configuracion = intentar_leer_fichero(nombre_fichero)

    return configuracion

def intentar_leer_fichero(nombre_fichero):
    configuracion = None
    try:
        configuracion = read_description(nombre_fichero)
    except:
        print("Fichero en formato incorrecto o ilegible")
    return configuracion


""" Funcion que pide al usuario una query. Si la query no es valida lo vuelve a intentar. """


def leer_query():
    query = None
    while query is None:
        lectura_teclado = raw_input("Introduce query: ")
        query = construir_query(lectura_teclado)
    return query


def construir_query(cadena):
    query = None
    try:
        query = Query(cadena)
    except:
        print("Query en formato incorrecto")
    return query


""" Funcion que pide al usuario la descripcion del grafo. Si la descripcion no es valida lo vuelve a intentar. """


def leer_descripcion(conFichero):
    correcto = False
    while not correcto:
        string = raw_input("Introduce numero de vertices, aristas y el tiempo de comunicacion maximo: ")

        try:
            num_vertices, num_aristas, max_timestamp = [int(i) for i in string.split(' ')]
        except:
            print("Descripcion en formato incorrecto")
            continue

        try:
            configuracion = random_graph(conFichero, num_vertices, num_aristas, max_timestamp)
        except:
            print("Error al crear el fichero")
            continue

        correcto = True

    return configuracion

def query_aleatorio(configuracion):
    max_vert = configuracion.get_num_vertices()
    max_ts = configuracion.get_max_ts()
    # Elegir nodos aleatorios
    nodo_infectado = random.randrange(0, max_vert)
    nodo_consulta = random.randrange(0, max_vert)
    # Elegir timestamps
    ts_infeccion = random.randrange(0, max_ts)
    ts_consulta = random.randrange(ts_infeccion, max_ts)

    return Query(str(nodo_infectado) + " " + str(ts_infeccion) + " " + str(nodo_consulta) + " " + str(ts_consulta))

def n_queries_aleatorios(configuracion, n):
    resultado = []
    for i in range(0, n):
        resultado.append(query_aleatorio(configuracion))
    return resultado


########################################################################################################################
##########################################         MAIN         ########################################################
########################################################################################################################

fichero_referencia = False

print("Introduce un comando:")
print("c - cambiar fichero de referencia")
print("q - realizar una query con metodo 1")
print("q - realizar una query con metodo 2")
print("v - visualizar el fichero de referencia")
print("r - crear un grafo aleatorio en memoria")
print("rf - crear un grafo aleatorio y cargarlo en memoria")
print("cc - comprobar correccion")
print("h - ayuda")

while True:

    comando = raw_input("$$: ")

    if (comando == "c"):
        configuracion = leer_nombre_fichero()
        fichero_referencia = True
    elif (comando == "q"):
        if fichero_referencia == False:
            print("  Error, no se ha cargado ningun grafo sobre el que realizar queries")
            continue
        query = leer_query()
        cProfile.run('configuracion.do(query)')
        infectado = configuracion.do(query)
        if infectado:
            print("Nodo infectado")
        else:
            print("Nodo no infectado")
    elif (comando == "q2"):
        if fichero_referencia == False:
            print("  Error, no se ha cargado ningun grafo sobre el que realizar queries")
            continue
        query = leer_query()
        cProfile.run('configuracion.do2(query)')
        infectado = configuracion.do2(query)
        if infectado:
            print("Nodo infectado")
        else:
            print("Nodo no infectado")
    elif (comando == "h"):
        muestra_ayuda()
    elif (comando == "v"):
        configuracion.dibujar()
        fichero_referencia = True
    elif (comando == "rf"):
        configuracion = leer_descripcion(True)
        fichero_referencia = True
    elif (comando == "cc"):
        configuracion = leer_descripcion(True)
        # Generar queries aleatorias para ese grafo
        n = 10
        queries = n_queries_aleatorios(configuracion, n)
        correctos = 0
        for query in queries:
            # TODO: Revisar por que da index out of range en configuracion.do
            infectado = configuracion.do(query)
            infectadoBFS = configuracion.BFS(query)
            if infectado == infectadoBFS:
                correctos += 1
        print(str(correctos) + " queries correctas de " + str(n) + " pruebas")
    elif (comando == "r"):
        configuracion = leer_descripcion(False)
        fichero_referencia = True
    else:
        print("Comando incorrecto")
        muestra_ayuda()

    print("Introduce un comando:")
