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
        for j in coladeNuevos:
            if i != j:
                coladeNuevos.remove(i)
    return coladeNuevos


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
            #print(i.idProceso)
            for j in range(len(particiones)):
            #print(i.tamanio)
            #print(particiones[j].tamanio)
             if i.tamanio <= particiones[j].tamanio and i.asignado != 1 and particiones[j].estado == 0:
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

def asignarCpu(coladeAsignados):
    global tiempo
    global procesador
    if coladeAsignados:
        if procesador.idProcesoAsignado == 0:
          procesador.idProcesoAsignado = coladeAsignados[0].idProceso
          procesador.tiempoDeAsignacion = tiempo
          procesador.tiempoDeIrrupcion = coladeAsignados[0].tiempoIrrupcion
          coladeNuevos.remove(coladeAsignados[0])
          coladeAsignados.remove(coladeAsignados[0])
          
          

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
print('------------------------------------')
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
        print('------------------------------------')

    if x == '2':
        # procesos en memoria
        print('Instancia de tiempo ' + str(tiempo))
        #print('------------------------------------')
        print('Listado de Procesos nuevos ')
        listadoProcesos(Nuevos())
        
        print('Asignacion de memoria')
        asignacionMemoria(coladeNuevos)
        print('Procesos que han sido asignado a memoria')
        listadoProcesos(coladeAsignados)
        print('------------------------------------')
        asignarCpu(coladeAsignados)
        print('------------------------------------')
        print('Proceso actualmente en CPU: ' + str(procesador.idProcesoAsignado) + ' (0 indica CPU desocupado')
        print('------------------------------------')
        print('Procesos que han sido asignado a memoria pero todavia no se han ejecutado')
        #eliminar()
        listadoProcesos(coladeNuevos)
        print('------------------------------------')
        # Eliminar procesos que ya termino de ejecutar
        # #print('procesador.tiempoDeAsignacion ' + str(procesador.tiempoDeAsignacion) +  ' procesador.tiempoDeIrrupcion ' + str(procesador.tiempoDeIrrupcion))
        controlProcesos()
        print('Procesos terminados concluida la instancia de tiempo '+ str(tiempo))
        listadoProcesos(colaTerminados)
        asignarCpu(coladeAsignados) #############
        tiempo += 1
        procesador.tiempoTranscurrido +=1
    if x == 'q':
        ejecucion = False


#sacar de memoria procesos terminados       LISTO
#marcar particiones ocmo desocupadas        LISTO
#cambiar cola de lsitos por cola de asignados en asignacion de cpu      LISTO
#mostrar tiempo transcurrido                LISTO
#cola de listos para procesos en memoria estado nuevo/suspendido para procesos ingresados   LISTO ??
#evitar que loopee el ingreso de procesos LISTO