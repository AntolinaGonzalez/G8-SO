# asignacion de procesos
proceso = [{'id': 'proce1', 'tamanio': 60, 'ta': 0, 'ti': 3}, {'id': 'proce2',
                                                               'tamanio': 100, 'ta': 0, 'ti': 2}, {'id': 'proce3', 'tamanio': 220, 'ta': 1, 'ti': 2}]
# asignacion de particiones
particion = [{'id': 'part1', 'tamanio': 100, 'estado': 1, 'fragmentacion': 0, 'tiempoSalida': None}, {'id': 'part2', 'tamanio': 250, 'estado': 0, 'fragmentacion': 0, 'tiempoSalida': None}, {
    'id': 'part3', 'tamanio': 120, 'estado': 0, 'fragmentacion': 0, 'tiempoSalida': None}, {'id': 'part4', 'tamanio': 60, 'estado': 0, 'fragmentacion': 0, 'tiempoSalida': None}]
# se ordenan las particiones ---a discutir----
particionOrdenada = sorted(particion, key=lambda i: i['tamanio'])

cola = []
auxiliar = []
ejecucion = True
tiempo = 0
colaTerminados = []

while ejecucion:
    print('El tiempo en curso: ' + str(tiempo))
    print()
    # se colocan los procesos en la cola de listos dependiendo de su ta
    for i in range(len(proceso)):
        if(proceso[i]['ta'] == tiempo):
            cola.append(proceso[i])

    cola = sorted(cola, key=lambda i: i['ti'])
    print('Cola de listos Ordenada antes de entrar a memoria: ')
    print(cola)
    print()
    for j in range(len(cola)):
        print('Proceso que va recorrer particiones')
        print(cola[j])
        print()
        for i in range(len(particionOrdenada)):
    
            if(particionOrdenada[i]['tamanio'] >= cola[j]['tamanio'] and particionOrdenada[i]['estado'] == 0):
                particionOrdenada[i]['estado'] = 1
                particionOrdenada[i]['fragmentacion'] = particionOrdenada[i]['tamanio'] - \
                    cola[j]['tamanio']
                particionOrdenada[i]['tiempoSalida'] = tiempo + cola[j]['ti']

                print('entro a memoria el proceso : ')
                print(cola[j])
                # cola.remove(cola[j])
                # print('colas con remove')
                # print(cola)
                print()
                print('se uso la particion')
                print(particionOrdenada[i])
                auxiliar.append(cola[j])
                break
            else:
                print('no ingreso a memoria el proceso: ')
                print(cola[j])
        
    for i in range(len(auxiliar)):
        cola.remove(auxiliar[i])
    
    auxiliar=[]

    for i in range(len(particionOrdenada)):
        if(particionOrdenada[i]['tiempoSalida']) == tiempo:
            #aca se debe agregar los procesos terminados
            colaTerminados.append(1)
            particionOrdenada[i]['estado'] = 0
            particionOrdenada[i]['fragmentacion'] = 0
            particionOrdenada[i]['salida'] = 0
    print()
    print('memoria en curso: ')
    print(particion)
    print()
    print('procesos terminados')
    print(colaTerminados)
    tiempo = tiempo+1
    # if tiempo == 7:
    #     print('algo sigue mal')
    #     ejecucion = False

    #controla que la cantidad de procesos terminados sea igual a los procesos que se habian solicitado
    if len(colaTerminados) == len(proceso):
        print('#No hay mas procesos a ejecutar')
        ejecucion = False
