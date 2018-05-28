# Tipo abstracto query
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

"""
    Clase que representa una consulta sobre un grafo. La consulta posee un nodo inicial de infeccion, un timestamp
    inicial de infeccion y un nodo que se quiere consultar si esta infectado para un timestamp concreto.
"""

class Query:

    # Constructor de la clase Query
    def __init__(self, string):
        nodo_infectado, timestamp_infeccion, nodo_consulta, timestamp_consulta = [int(i) for i in string.split(' ')]
        self.nodo_infectado = nodo_infectado
        self.nodo_consulta = nodo_consulta
        self.timestamp_infeccion = timestamp_infeccion
        self.timestamp_consulta = timestamp_consulta

    # Obtiene el nodo inicial de la infeccion
    def get_nodo_infectado(self):
        return self.nodo_infectado

    # Obtiene el nodo a consultar
    def get_nodo_consulta(self):
        return self.nodo_consulta

    # Obtiene el instante inicial de la infeccion
    def get_timestamp_infeccion(self):
        return self.timestamp_infeccion

    # Obtiene el instante de la consulta
    def get_timestamp_consulta(self):
        return self.timestamp_consulta
