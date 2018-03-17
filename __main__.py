# Programa Principal. Lectura de ficheros y querys
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

from description_file_reader import read_description
from Query import Query


########################################################################################################################
#############################         Funciones de entrada de comandos         #########################################
########################################################################################################################

def muestra_ayuda():
    print(" El comando 'c' permite cambiar fichero de referencia")
    print(" Este fichero debe seguir el siguiente formato:")
    #TODO: Especificar formato de los ficheros de entradaa
    print(" El comando 'q' permite introducir una query al sistema")
    print(" La query debe tener el siguiente formato:")
    #TODO: Especificar el forma de las querys

""" Funcion que pide al usuario el nombre de un fichero y lo intenta interpretar. Si el fichero no es valido lo vuelve
    a intentar. """
def leer_nombre_fichero():
    correcto = False
    while not correcto:
        nombre_fichero = input("Introduce fichero de entrada: ")

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
        lectura_teclado = input("Introduce query: ")

        try:
            query = Query(lectura_teclado)
            correcto = True
        except:
            print("Query en formato incorrecto")

    return query



########################################################################################################################
##########################################         MAIN         ########################################################
########################################################################################################################

configuracion = leer_nombre_fichero()

print("Introduce un comando:")
print("c - cambiar fichero de referencia")
print("q - realizar una query")
print("h - ayuda")

while True:

    comando = input("$$: ")

    if(comando == "c"):
        configuracion = leer_nombre_fichero()
    elif(comando == "q"):
        query = leer_query()
        configuracion.do(query)
        #TODO: ALgoritmo voraz
    elif(comando == "h"):
        muestra_ayuda()
    else:
        print("Comando incorrecto")
        muestra_ayuda()


    print("Introduce un comando:")
