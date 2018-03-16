# Tipo abstracto query
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

class Query:

    def __init__(self,string):
        nodo_infectado, nodo_consulta, timestamp_infeccion, timestamp_consulta = [int(i) for i in lineas[0].split(' ')]
        self.nodo_infectado = nodo_infectado
        self.nodo_consulta = nodo_consulta
        self.timestamp_infeccion = timestamp_infeccion
        self.timestamp_consulta  = timestamp_consulta