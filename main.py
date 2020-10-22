from repository import *

# variables globables
ejecucion = True
procesos = []
tiempo = 0
coladeListos = []
colaTerminados = []
procesosAsignar = []

print('---------------Particiones---------------')
for i in particiones:
    print(i.idParticion)
    print(i.tamanio)
    print(i.estado)

# listado de procesos


def listadoProcesos(proceso):
    for i in proceso:
        print('------------------------------------')
        print('id: ' + str(i.idProceso))
        print('tamanio: ' + str(i.tamanio))
        print('tiempo de arribo: ' + str(i.tiempoArribo))
        print('tiempo de irrupcion: '+str(i.tiempoIrrupcion))

# asignacion de un proceso


def CrearProceso():
    global procesos
    print('Ingrese un id y un tamanio un ta y un ti \n')

    idPart = int(input('Ingrese el id del proceso \n'))  # automatizar esto
    tamanio = int(input('Ingrese el tamanio del proceso\n'))
    ta = int(input('Ingrese el tiempo de arribo \n'))
    ti = int(input('Ingrese el tiempo de irrupcion ti\n'))
    proceso = Proceso(idPart, tamanio, ta, ti)
    procesos.append(proceso)
    procesos = sorted(
                procesos, key=lambda x: x.tiempoIrrupcion)


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


def asignacionMemoria(procesos):
    
    for i in procesos:
        bestFit=''
        tamanio=999999999
        print(i.idProceso)
        for j in particiones:
            print(i.tamanio)
            print(j.tamanio)
            if i.tamanio<= j.tamanio and tamanio>j.tamanio:
                print('entro')
                bestFit = j.idParticion
                tamanio = j.tamanio
                index = particiones.index()
        if bestFit!='':
            particiones[index].estado=1
    print('---------------Particiones---------------')
    for i in particiones:
        print(i.idParticion)
        print(i.tamanio)
        print(i.estado)




def controlSalidaProceso():
    pass


# creamos un proceso para iniciar
print(CrearProceso())
print('Lista de procesos \n')
listadoProcesos(procesos)
print('------------------------------------')

while ejecucion:
    # menu
    print('')
    x = input(
        '1. Cargar mas procesos \n2. Comenzar ejecucion de los procesos en memoria \n3.q para salir')
    if x == '1':
        # se crean procesos
        print(CrearProceso())
        print('Lista de procesos \n')
        # listado de procesos
        listadoProcesos(procesos)
        print('------------------------------------')

    if x == '2':
        # procesos en memoria
        Listos()
        print('listado de listos')
        listadoProcesos(coladeListos)
        print('------------------------------------')
        print('Asignacion de memoria')
        asignacionMemoria(coladeListos)
        tiempo += 1
    if x == 'q':
        ejecucion = False
