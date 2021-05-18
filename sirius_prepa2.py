# Realice un programa que simule la base de datos (Usando listas) de "Sirius".
# En este sentido, se requiere un programa que realice las operaciones básicas CRUD

#Create ===> Crear un estudiante con la información pertinente y agregarlo a la base de datos
#Read ===> Consultar todos los estudiantes de la base de datos de forma ordenada indicando la información de ese estudiante
#Update===> Manejar una opción para actualizar alguno de los datos de un estudiante en especifico.
#Delete ===> Eliminar el estudiante de la base de datos, eliminando así toda la información relacionada a ese estudiante en especifico

#Donde la información importante en relación a la base de datos son: El nombre del estudiante, la cedula, edad y las materias que cursa ese estudiante.
base_de_datos=[]
materia=[]
m=False
while m==False:
    menu= input('1.Agregar estudiante\n2.Eliminar estudiante\n3.Mostrar base de datos de estudiantes registrados\n4.Actualizar información\n')
    if menu.isnumeric():
        if menu==1:
            nuevo_estudiante=input('Ingresar nombre del nuevo estudiante: ').lower()
            edad=input('Ingresar edad del nuevo estudiante: ')
            cedula=input('Ingresar cédula del nuevo estudiante: ')
            numero_de_materias=input('Ingresar número de materias a cursar: ')
            i=0
            while i<numero_de_materias:
                materias_cursar=input('Ingresar materia a cursar: ').lower()
                materia.append(materias_cursar)
                i+=1
            base_de_datos=[nuevo_estudiante[edad,cédula,materia]]
            c=input('Desea continuar? (y o n): ').lower()
            if c=='n':
                m=True
            else:
                m=False
        if menu==2:
            print(base_de_datos)
            eliminar_estudiante=input('Ingresar nombre del estudiante: ').lower()
            if eliminar_estudiante in base_de_datos:
                base_de_datos.remove(eliminar_estudiante)
                c=input('Desea continuar? (y o n): ').lower()
                if c=='n':
                    m=True
                else:
                    m=False
            else:
                print('Dato incorrecto, intenta de nuevo')
        if menu==3:
            print(base_de_datos)
            c=input('Desea continuar? (y o n): ').lower()
            if c=='n':
                m=True
            else:
                m=False
        if menu==4:
            print(base_de_datos)
            usuario_informacion=input('Ingresar nombre del usuario: ').lower()
            if usuario_informacion in base_de_datos:
                actualizar_informacon=input('1.Edad\n2.Cédula\n3.Materias\n')
                if actualizar_informacon==1:
                    cambio_edad=input('Ingresa el nuevo dato: ')
                    for i in base_de_datos.index(usuario_informacion):
                        edad=cambio_edad
                    c=input('Desea continuar? (y o n): ').lower()
                    if c=='n':
                        m=True
                    else:
                        m=False
                elif actualizar_informacon==2:
                    cambio_cedula=input('Ingresa el nuevo dato: ')
                    for i in base_de_datos.index(usuario_informacion):
                        cédula=cambio_cedula
                    c=input('Desea continuar? (y o n): ').lower()
                    if c=='n':
                        m=True
                    else:
                        m=False
                elif actualizar_informacon==3:
                    agregar_materia=input('Ingresa el nuevo dato: ').lower()
                    for i in base_de_datos.index(usuario_informacion):
                        materia.append(agregar_materia)
                    c=input('Desea continuar? (y o n): ').lower()
                    if c=='n':
                        m=True
                    else:
                        m=False
                else:
                    print('Dato incorrecto, intenta de nuevo')
            else:
                print('Dato incorrecto, intenta de nuevo')
        else:
            print('Dato incorrecto, intenta de nuevo')
    else:
        print('Dato incorrecto, intenta de nuevo')
print('Sesión terminada')