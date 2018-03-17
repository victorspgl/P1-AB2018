# Tipo abstracto Arista
# Javier Corbalan y Victor Soria
# 15 Marzo 2018

class Arista:

    def __init__(self, vertice_inicial, vertice_final, timestamp):
        self.vertice_inicial = vertice_final
        self.vertice_final   = vertice_final
        self.timestamp       = timestamp

    def get_timestamp(self):
        return self.timestamp

    def get_vertice_inicial(self):
        return self.vertice_inicial

    def get_vertice_final(self):
        return self.vertice_final

    def get_timestamp(self):
        return self.timestamp