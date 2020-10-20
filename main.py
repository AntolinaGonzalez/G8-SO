from repository import *

# variables globables
ejecucion = True
procesos = []
tiempo = 0
coladeListos = []
colaTerminados = []


print('---------------Particiones---------------')
for i in particiones:
    print(i.idParticion)
    print(i.tamanio)

# asignacion de un proceso


def CrearProceso():
    print('Ingrese un id y un tamanio un ta y un ti \n')

    x = int(input('id \n'))
    y = int(input('tamanio\n'))
    z = int(input('ta\n'))
    w = int(input('ti\n'))
    return Procesos(x, y, z, w)


def Procesos(id, tamanio, ta, ti):
    proceso = Proceso(id, tamanio, ta, ti)
    procesos.append(proceso)
    return proceso.idProceso

# cola de listos


def Listos():
    global tiempo
    global coladeListos
    for i in procesos:
        if i.tiempoArribo == tiempo:
            coladeListos.append(i)
            # Ordenar teniendo en cuenta el tiempo de irrupcion
            coladeListos = sorted(
                coladeListos, key=lambda x: x.tiempoIrrupcion)
    return coladeListos

def asignacionMemoria():
    pass

def controlSalidaProceso():
    pass

#creamos un proceso para iniciar
print(CrearProceso())
print('Lista de procesos \n')
for i in range(len(procesos)):
    print(procesos[i].idProceso)

while ejecucion:
    #menu
    x = input(
        '1. Cargar mas procesos \n2. Comenzar ejecucion de los procesos en memoria \n3.q para salir')
    if x == '1':
        #se crean procesos
        print(CrearProceso())
        print('Lista de procesos \n')
        for i in procesos:
            print(i.idProceso)
    if x == '2':
        # procesos en memoria
        for i in Listos():
            print('primero' + str(i.idProceso))
            print(i.tiempoArribo)
            print(i.tiempoIrrupcion)
        tiempo += 1
