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


class Particion:
    def __init__(self, idParticion, tamanio):
        self.idParticion = idParticion
        self.tamanio = tamanio
        self.fragmentacion = 0
        self.estado = 0
        self.tiempoSalida = None
        self.proceso = None

#creacion de particiones
particion1=Particion('SO',100)
particiones.append(particion1)
particion2=Particion('Part1', 250)
particiones.append(particion2)
particion3=Particion('part2',120)
particiones.append(particion3)
particion4=Particion('part3',60)
particiones.append(particion4)