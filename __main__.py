# Programa Principal. Lectura de ficheros y querys
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

from random_tools import random_graph
from random_tools import n_queries_aleatorios
from description_file_reader import read_description_graph
from description_file_reader import read_description_queries
from Query import Query
import time


########################################################################################################################
#############################         Funciones de entrada de comandos         #########################################
########################################################################################################################

"""
    Muestra por pantalla un resumen de los comandos que se pueden ejecutar
"""

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
    print(" El comando 'gq' permite generar un numero aleatorio de queries sobre un grafo")
    print(" El comando 'cc' permite validar y medir el tiempo de ejecucion de un fichero de queries y un grafo")



""" 
    Funcion que pide al usuario el nombre de un fichero y lo intenta interpretar como grafo. Si el fichero no es valido
    lo vuelve a intentar.
"""

def leer_nombre_fichero():
    configuracion = None
    while configuracion is None:
        nombre_fichero = raw_input("Introduce fichero de entrada: ")
        configuracion = intentar_leer_fichero_grafo(nombre_fichero)

    return configuracion

"""
    Funcion que encapsula el tratamiento de errores de la funcion read_description_graph
"""
def intentar_leer_fichero_grafo(nombre_fichero):
    configuracion = None
    try:
        configuracion = read_description_graph(nombre_fichero)
    except:
        print("Fichero en formato incorrecto o ilegible")
    return configuracion



""" 
    Funcion que pide al usuario una query. Si la query no es valida lo vuelve a intentar.
"""
def leer_query(configuracion):
    query = None
    while query is None:
        lectura_teclado = raw_input("Introduce query: ")
        nodo_infectado, timestamp_infeccion, nodo_consulta, timestamp_consulta = [int(i) for i in lectura_teclado.split(' ')]
        if(nodo_consulta > configuracion.num_vertices or nodo_infectado > configuracion.num_vertices or
           nodo_infectado < 0 or nodo_consulta < 0 or timestamp_consulta < 0 or timestamp_infeccion < 0):
            print("Query incorrecta")
            continue
        query = construir_query(lectura_teclado)
    return query


"""
    Funcion que encapsula el tratamiento de errores en la clase Query
"""
def construir_query(cadena):
    query = None
    try:
        query = Query(cadena)
    except:
        print("Query en formato incorrecto")
    return query



"""
    Funcion que pide al usuario la descripcion del grafo. Si la descripcion no es valida lo vuelve a intentar.
"""
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

"""
    Funcion que pide al usuario el nombre de un fichero y lo intenta interpretar como una lista de queries. Si el
    fichero no es valido lo vuelve a intentar.
"""
def leer_fichero_query():
    queries = None
    while queries is None:
        nombre_fichero = raw_input("Introduce fichero de entrada de queries: ")
        queries = intentar_leer_fichero_queries(nombre_fichero)

    return queries

"""
    Funcion que encapsula el tratamiento de errores de la funcion read_description_queries
"""
def intentar_leer_fichero_queries(nombre_fichero):
    configuracion = None
    try:
        configuracion = read_description_queries(nombre_fichero)
    except:
        print("Fichero en formato incorrecto o ilegible")
    return configuracion



########################################################################################################################
##########################################         MAIN         ########################################################
########################################################################################################################

fichero_referencia = False

print("Introduce un comando:")
print("c - cambiar fichero de referencia")
print("q - realizar una query con metodo 1")
print("q2 - realizar una query con metodo 2")
print("r - crear un grafo aleatorio en memoria")
print("rf - crear un grafo aleatorio en un fichero y cargarlo en memoria")
print("gq - generar un fichero con querys aleatorias")
print("cc - comprobar correccion")
print("t - obtener los tiempos de ejecucion")
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
        query = leer_query(configuracion)
        start = time.time()
        infectado = configuracion.do(query)
        end = time.time()
        print("Tiempo de ejecucion " + str(end - start) + " segundos")

        if infectado:
            print("Nodo infectado")
        else:
            print("Nodo no infectado")
    elif (comando == "q2"):
        if fichero_referencia == False:
            print("  Error, no se ha cargado ningun grafo sobre el que realizar queries")
            continue
        query = leer_query(configuracion)
        start = time.time()
        infectado = configuracion.do2(query)
        end = time.time()
        print("Tiempo de ejecucion " + str(end - start) + " segundos")
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
    elif (comando == "gq"):
        if fichero_referencia == False:
            print("  Error, no se ha cargado ningun grafo sobre el que realizar queries")
            continue
        n = 20
        queries = n_queries_aleatorios(configuracion, n)
    elif (comando == "cc"):
        configuracion = leer_nombre_fichero()
        queries = leer_fichero_query()
        correctos = 0
        for query in queries:
            infectado = configuracion.do(query)
            infectado2 = configuracion.do2(query)
            if infectado == infectado2:
                correctos += 1
        print(str(correctos) + " queries correctas de " + str(len(queries)) + " pruebas")
    elif (comando == "t"):
        configuracion = leer_nombre_fichero()
        queries = leer_fichero_query()
        tiempos_alg1 = []
        tiempos_alg2 = []
        for query in queries:
            start = time.time()
            infectado = configuracion.do(query)
            end = time.time()
            tiempos_alg1.append(end-start)

            start = time.time()
            infectado2 = configuracion.do2(query)
            end = time.time()
            tiempos_alg2.append(end-start)


        cadena  = "Tiempos por query "
        cadena1 = "Metodo 1:         "
        cadena2 = "Metodo 2:         "
        for i in range(0,len(queries)):
            cadena  = cadena  + "  q" + str(format(i+1,'2.0f')) + "   "
            cadena1 = cadena1  + str(format(tiempos_alg1[i],'2.3f')) + "   "
            cadena2 = cadena2 + str(format(tiempos_alg2[i],'2.3f')) + "   "
        print(cadena)
        print(cadena1)
        print(cadena2)

    elif (comando == "r"):
        configuracion = leer_descripcion(False)
        fichero_referencia = True
    else:
        print("Comando incorrecto")
        muestra_ayuda()

    print("Introduce un comando:")
