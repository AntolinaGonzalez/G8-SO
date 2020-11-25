from repository import *

# variables globables
ejecucion = True
procesos = []
tiempo = 0
coladeNuevos = []
coladeAsignados = []
colaTerminados = []
procesosAsignar = []
id_proceso = 0


def particioneslistado():
    print('----------------------------------------------Particiones---------------------------------------------------------')
    espacio = '             '
    # for i in particiones:
    #     print('id de la Particion: ' + str(i.idParticion))
    #     print('tamanio de la particion: ' + str(i.tamanio))
    #     print('estado de la particion: ' + str(i.estado))
    #     print('fragmentacion interna: ' + str(i.fragmentacion) + 'Kb')
    #     print('----------------------------------------------')
    print('     id Particion           |       Tamanio               |       Estado              |       Fragmentacion         |')
    print('-------------------------------------------------------------------------------------------------------------------')
    print(espacio + str(particiones[0].idParticion) + espacio + '|' + espacio + str(particiones[0].tamanio) + espacio + '|' +
          espacio + str(particiones[0].estado) + espacio + '|' + espacio + str(particiones[0].fragmentacion) + espacio + '  |')
    print('-------------------------------------------------------------------------------------------------------------------')
    print(espacio + str(particiones[1].idParticion) + espacio + ' |' + espacio + str(particiones[1].tamanio) + espacio + '|' +
          espacio + str(particiones[1].estado) + espacio + ' |' + espacio + str(particiones[1].fragmentacion) + espacio + ' |')
    print('-------------------------------------------------------------------------------------------------------------------')
    print(espacio + str(particiones[2].idParticion) + espacio + ' |' + espacio + str(particiones[2].tamanio) + espacio + '|' +
          espacio + str(particiones[2].estado) + espacio + ' |' + espacio + str(particiones[2].fragmentacion) + espacio + ' |')
    print('-------------------------------------------------------------------------------------------------------------------')
    print(espacio + str(particiones[3].idParticion) + espacio + ' |' + espacio + str(particiones[3].tamanio) + espacio + ' |' +
          espacio + str(particiones[3].estado) + espacio + ' |' + espacio + str(particiones[3].fragmentacion) + espacio + ' |')

# listado de procesos


def listadoProcesos(proceso):
    espacio = '            '
    print('     id Proceso          |       Tamanio             |    Tiempo de arribo     |   Tiempo de irrupcion   |')
    print('---------------------------------------------------------------------------------------------------------|')
    for i in proceso:
        if i.tamanio > 99:
            print(espacio + str(i.idProceso) + espacio + '|' + espacio + str(i.tamanio) + espacio + '|' +
                  espacio + str(i.tiempoArribo) + espacio + '|' + espacio + str(i.tiempoIrrupcion) + espacio + '|')
            print('---------------------------------------------------------------------------------------------------------|')
        else:
            print(espacio + str(i.idProceso) + espacio + '|' + espacio + str(i.tamanio) + espacio + ' |' +
                  espacio + str(i.tiempoArribo) + espacio + '|' + espacio + str(i.tiempoIrrupcion) + espacio + '|')
            print('---------------------------------------------------------------------------------------------------------|')

        # print('------------------------------------')
        # print('id: ' + str(i.idProceso))
        # print('tamanio: ' + str(i.tamanio))
        # print('tiempo de arribo: ' + str(i.tiempoArribo))
        # print('tiempo de irrupcion: ' + str(i.tiempoIrrupcion))


# eliminar procesos que ya fueron asignados

def eliminar():
    for i in coladeAsignados:
        for j in coladeNuevos:
            if j == i:
                coladeNuevos.remove(i)


# asignacion de un proceso


def CrearProceso():
    global procesos
    global id_proceso
    print()
    print('Ingrese la informacion de un proceso \n')

    id_proceso = id_proceso + 1
    idPart = id_proceso  # automatizar esto
    tamanio = int(input('Ingrese el tamanio del proceso\n'))
    ta = int(input('Ingrese el tiempo de arribo \n'))
    ti = int(input('Ingrese el tiempo de irrupcion ti\n'))
    proceso = Proceso(idPart, tamanio, ta, ti)
    procesos.append(proceso)
    # procesos = sorted(
    #     procesos, key=lambda x: x.tiempoIrrupcion)


def Nuevos():
    global tiempo
    global coladeNuevos
    global coladeAsignados
    for i in procesos:
        if i.tiempoArribo == tiempo:
            coladeNuevos.append(i)
            # Ordenar teniendo en cuenta el tiempo de irrupcion
            coladeNuevos = sorted(
                coladeNuevos, key=lambda x: x.tiempoIrrupcion)
    return coladeNuevos


def memoria(procesos):
    tamanio = 9999999
    id = -5
    for i in procesos:
        for j in particiones:
            if j.tamanio >= i.tamanio and j.tamanio < tamanio and j.estado == 0:
                tamanio = j.tamanio
                id = int(j.idParticion)
                proceso = i
                print('particiones')
        if id > 0:
            coladeAsignados.append(i)
            particiones[id].estado = 1
            particiones[id].fragmentacion = particiones[id].tamanio - \
                proceso.tamanio
            particiones[id].tiempoSalida = tiempo + proceso.tiempoIrrupcion
            particiones[id].proceso = proceso
            particiones[id].idProceso = proceso.idProceso
        tamanio = 9999999
        id = -5
    particioneslistado()


def asignacionMemoria(procesos):
    global coladeAsignados
    global particiones
    for i in procesos:
        if i.asignado != 1:
            bestFit = ''
            #tamanio = 999999999
            index = 0
            particiones = sorted(
                particiones, key=lambda z: z.tamanio)
            # print(i.idProceso)
            for j in range(len(particiones)):
                # print(i.tamanio)
                # print(particiones[j].tamanio)
                if i.tamanio <= particiones[j].tamanio and i.asignado != 1 and particiones[j].estado == 0:
                    if particiones[j].estado == 0:
                        print('Proceso ' + str(i.idProceso) +
                              ' asignado a particion ' + str(particiones[j].idParticion))
                        bestFit = particiones[j].idParticion
                        tamanio = particiones[j].tamanio
                        index = j
                        i.asignado = 1
                        particiones[j].idProceso = i.idProceso
                        coladeAsignados.append(i)
                    if bestFit != '':
                        particiones[index].estado = 1
                        particiones[index].fragmentacion = particiones[index].tamanio - i.tamanio
                        particiones[index].tiempoSalida = tiempo + \
                            i.tiempoIrrupcion
                        particiones[index].proceso = i
                        particiones[j].idProceso = i.idProceso

    particioneslistado()


def asignarCpu(coladeAsignados):
    global tiempo
    global procesador
    if coladeAsignados:
        if procesador.idProcesoAsignado == 0:
            procesador.idProcesoAsignado = coladeAsignados[0].idProceso
            procesador.tiempoDeAsignacion = tiempo
            procesador.tiempoDeIrrupcion = coladeAsignados[0].tiempoIrrupcion
            coladeAsignados.remove(coladeAsignados[0])


def controlProcesos():
    global tiempo
    global procesador
    if (tiempo - procesador.tiempoDeAsignacion == procesador.tiempoDeIrrupcion):
        for i in particiones:
            if i.idProceso == procesador.idProcesoAsignado:
                colaTerminados.append(i.proceso)
                procesador.idProcesoAsignado = 0
                procesador.tiempoTranscurrido = 0
                i.fragmentacion = 0
                i.estado = 0
                i.tiempoSalida = None
                i.proceso = None
                i.idProceso = None


def controlSalidaProceso():
    pass


# visualizamos las particiones
particioneslistado()
# creamos un proceso para iniciar
print(CrearProceso())
print('Lista de procesos \n')
listadoProcesos(procesos)
x = '0'


while ejecucion:
    # menu
    print('')
    if x != '2':
        x = input(
            '1. Cargar mas procesos \n2. Ejecucion de los procesos en memoria \n3.q para salir\n')
    else:
        input('Presione cualquier tecla para continuar la ejecución de los procesos ya cargados')
    if x == '1':
     # se crean procesos
        print(CrearProceso())
        print('Lista de procesos \n')
        # listado de procesos
        listadoProcesos(procesos)

    if x == '2':
        # procesos en memoria
        print('-------------------------')
        print('| Instancia de tiempo ' + str(tiempo) + ' |')
        print('-------------------------')
        print()
        # print('------------------------------------')
        print('Listado de Procesos nuevos ')
        print('---------------------------')
        print()
        listadoProcesos(Nuevos())
        print()
        print('Asignacion de memoria')
        print('----------------------')
        memoria(coladeNuevos)
        print()
        eliminar()
        asignarCpu(coladeAsignados)
        print()
        print('Proceso actualmente en CPU: ' +
              str(procesador.idProcesoAsignado) + ' (0 indica CPU desocupado')
        print('------------------------------------------')
        print()
        print('Procesos que han sido asignado a memoria pero todavia no se han ejecutado')
        print('--------------------------------------------------------------------------')
        # eliminar()
        listadoProcesos(coladeAsignados)
        # Eliminar procesos que ya termino de ejecutar
        # #print('procesador.tiempoDeAsignacion ' + str(procesador.tiempoDeAsignacion) +  ' procesador.tiempoDeIrrupcion ' + str(procesador.tiempoDeIrrupcion))
        controlProcesos()
        print('Procesos terminados concluida la instancia de tiempo ' + str(tiempo))
        listadoProcesos(colaTerminados)
        asignarCpu(coladeAsignados)
        tiempo += 1
        procesador.tiempoTranscurrido += 1
    if x == 'q':
        ejecucion = False
