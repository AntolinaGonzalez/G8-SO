'''
Repositorio de clases
'''

particiones=[]
class Proceso:

    def __init__(self, idProceso, tamanio,  tiempoArribo, tiempoIrrupcion):
        self.idProceso = idProceso
        self.tamanio = tamanio
        self.tiempoArribo = tiempoArribo
        self.tiempoIrrupcion = tiempoIrrupcion
        self.asignado = 0


class Particion:
    def __init__(self, idParticion, tamanio):
        self.idParticion = idParticion
        self.tamanio = tamanio
        self.fragmentacion = 0
        self.estado = 0
        self.tiempoSalida = None
        self.proceso = None
        self.idProceso = None

class Cpu:
    def __init__ (self, idProcesoAsignado, tiempoDeAsignacion, tiempoIrrupcion):
        self.idProcesoAsignado = idProcesoAsignado
        self.tiempoTranscurrido = 0
        self.tiempoDeAsignacion = 0
        self.tiempoIrrupcion = tiempoIrrupcion



#creacion de particiones
particion1=Particion('SO',100)
particiones.append(particion1)
particiones[0].estado = 1
particion2=Particion('1', 250)
particiones.append(particion2)
particion3=Particion('2',120)
particiones.append(particion3)
particion4=Particion('3',60)
particiones.append(particion4)

#inicializacion de cpu
procesador = Cpu(0,0,0)