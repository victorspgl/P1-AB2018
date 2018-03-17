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

    def get_nodo_infectado(self):
        return self.nodo_infectado

    def get_nodo_consulta(self):
        return self.nodo_consulta

    def get_timestamp_infeccion(self):
        return self.timestamp_infeccion