'''
Repositorio de clases 
'''


class Proceso:
    def __init__(self, idProceso, tamanio, tiempoArribo, tiempoIrrupcion):
        self.idProceso=idProceso
        self.tamanio=tamanio
        self.tiempoArribo=tiempoArribo
        self.tiempoIrrupcion=tiempoIrrupcion

class Particion:
    def __init__(self, idParticion, tamanio, dirInicio):
        self.idParticion=idParticion
        self.tamanio=tamanio
        self.dirInicio=dirInicio
        self.fragmentacion=0
        self.estado = 0
        self.proceso=None