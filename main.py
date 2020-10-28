from repository import *

# variables globables
ejecucion = True
procesos = []
tiempo = 0
coladeListos = []
coladeAsignados = []
colaTerminados = []
procesosAsignar = []
id_proceso = 0


def particioneslistado():
    print('---------------Particiones---------------')
    for i in particiones:
        print('id de la Particion: ' + str(i.idParticion))
        print('tamanio de la particion: ' + str(i.tamanio))
        print('estado de la particion: ' + str(i.estado))
        print('fragmentacion interna: ' + str(i.fragmentacion) + 'Kb')
        print('----------------------------------------------')


# listado de procesos


def listadoProcesos(proceso):
    for i in proceso:
        print('------------------------------------')
        print('id: ' + str(i.idProceso))
        print('tamanio: ' + str(i.tamanio))
        print('tiempo de arribo: ' + str(i.tiempoArribo))
        print('tiempo de irrupcion: ' + str(i.tiempoIrrupcion))


# eliminar procesos que ya fueron asignados


def eliminar():
    for i in coladeAsignados:
        for j in coladeListos:
            if i == j:
                coladeListos.remove(i)
    return coladeListos


# asignacion de un proceso


def CrearProceso():
    global procesos
    global id_proceso
    print()
    print('Ingrese un la informacion de un proceso \n')

    id_proceso = id_proceso + 1
    idPart = id_proceso  # automatizar esto
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
    global coladeAsignados
    for i in procesos:
        if i.tiempoArribo == tiempo:
            coladeListos.append(i)
            # Ordenar teniendo en cuenta el tiempo de irrupcion
            coladeListos = sorted(
                coladeListos, key=lambda x: x.tiempoIrrupcion)
    return coladeListos


def asignacionMemoria(procesos):
    global coladeAsignados
    global particiones
    for i in procesos:
        if i.asignado != 1:
            bestFit = ''
            tamanio = 999999999
            index = 0
            #print(i.idProceso)
            for j in range(len(particiones)):
            #print(i.tamanio)
            #print(particiones[j].tamanio)
             if i.tamanio <= particiones[j].tamanio and tamanio > particiones[j].tamanio and i.asignado != 1:
                particiones = sorted(
                    particiones, key=lambda z: z.tamanio)
                if particiones[j].estado == 0:
                    print('Proceso ' + str(i.idProceso) +' asignado a particion ' +str(particiones[j].idParticion))
                    bestFit = particiones[j].idParticion
                    tamanio = particiones[j].tamanio
                    index = j
                    i.asignado = 1
                    particiones[j].idProceso = i.idProceso
                    coladeAsignados.append(i)
                if bestFit != '':
                     particiones[index].estado = 1
                     particiones[index].fragmentacion = particiones[index].tamanio - i.tamanio
                     particiones[index].tiempoSalida = tiempo + i.tiempoIrrupcion
                     particiones[index].proceso = i
                     particiones[j].idProceso = i.idProceso

    particioneslistado()


#def controlProcesos():
#    global tiempo
#    for i in particiones:
#        if tiempo == i.tiempoSalida:
#            colaTerminados.append(i.proceso)
#            i.estado = 0
#            i.fragmentacion = 0
#            i.tiempoSalida = 0
#            i.proceso = None

def asignarCpu(coladeListos):
    global tiempo
    global procesador
    if procesador.idProcesoAsignado == 0:

        coladeListos = sorted(coladeListos, key=lambda z: z.tiempoArribo)
        procesador.idProcesoAsignado = coladeListos[0].idProceso
        procesador.tiempoDeAsignacion = tiempo
        procesador.tiempoDeIrrupcion = coladeListos[0].tiempoIrrupcion


#def controlProcesos():
#    global tiempo
#    for i in particiones:
#        if tiempo == i.tiempoSalida:
#            colaTerminados.append(i.proceso)
#            i.estado = 0
#            i.fragmentacion = 0
#            i.tiempoSalida = 0
#            i.proceso = None

def controlProcesos():
    global tiempo
    global procesador
    if (tiempo - procesador.tiempoDeAsignacion == procesador.tiempoDeIrrupcion):
        for i in particiones:
            if i.idProceso == procesador.idProcesoAsignado:
                colaTerminados.append(i.proceso)
                procesador.idProcesoAsignado = 0
                procesador.tiempoTranscurrido = 0

def controlSalidaProceso():
    pass


# visualizamos las particiones
particioneslistado()
# creamos un proceso para iniciar
print(CrearProceso())
print('Lista de procesos \n')
listadoProcesos(procesos)
print('------------------------------------')



while ejecucion:
    # menu
    print('')
    x = input(
        '1. Cargar mas procesos \n2. Ejecucion de los procesos en memoria \n3.q para salir\n')
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
        print('Procesos que fueron guardados en memoria')
        listadoProcesos(coladeAsignados)
        print('------------------------------------')
        asignarCpu(coladeListos)
        print('Proceso actualmente en CPU: ' + str(procesador.idProcesoAsignado))
        print('------------------------------------')
        print('procesos que aun se encuentran en la cola de listos')
        eliminar()
        listadoProcesos(coladeListos)
        print('------------------------------------')
        # Eliminar procesos que ya termino de ejecutar
        controlProcesos()
        print('Procesos que terminaron')
        listadoProcesos(colaTerminados)
        tiempo += 1
        procesador.tiempoTranscurrido +=1
    if x == 'q':
        ejecucion = False
