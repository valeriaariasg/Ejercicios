# Realice un programa que simule la base de datos (Usando listas) de "Sirius".
# En este sentido, se requiere un programa que realice las operaciones básicas CRUD

#Create ===> Crear un estudiante con la información pertinente y agregarlo a la base de datos
#Read ===> Consultar todos los estudiantes de la base de datos de forma ordenada indicando la información de ese estudiante
#Update===> Manejar una opción para actualizar alguno de los datos de un estudiante en especifico.
#Delete ===> Eliminar el estudiante de la base de datos, eliminando así toda la información relacionada a ese estudiante en especifico

#Donde la información importante en relación a la base de datos son: El nombre del estudiante, la cedula, edad y las materias que cursa ese estudiante.

nombre= input('Ingrese nombre: ').lower()
s=input('Ingrese su nombre de usuario sirius: ')
estudiantes=[]
materia= []
datos=[]
datos=s

abierto=False
while abierto==False:
    for i in estudiantes:
        if nombre==estudiantes.index(s):
            dato=False
            while dato==False:
                opcion=int(input('Elegir\n1.Actualizar:\n2.Eliminar: '))
                if opcion.isnumeric:
                    if opcion==1:
                        print(estudiantes)
                        actualizar=int(input('Actualizar\n1.Cédula\n2.Materia\n3.Edad'))
                        if actualizar==1:
                            oci=input('Ingrese su cédula anterior: ')
                            nci=input('Ingrese su cédula nueva: ')
                            for i in estudiantes:
                                if oci==estudiantes.index(s):
                                    estudiantes[i]=nci
                                    print('Actualización exitosa')
                                    print(estudiantes)
                                    dato=True
                                else:
                                    print(f'No existe la cédula {oci}, intente de nuevo')
                                    dato=False
                        elif actualizar==2:
                            materias=input('Ingrese su materia nueva: ').lower()
                            s=[materia.append(materias)]
                            print('Actualización exitosa')
                            print(estudiantes)
                            dato=True
                        elif actualizar==3:
                            en=input('Ingrese su nueva edad: ')
                            for i in s:
                                if en-1 == s[i]:
                                    s[i]=en
                                    print('Actualización exitosa')
                                    print(estudiantes)
                                    dato=True
                        else:
                            print('Dato incorrecto, inténtelo de nuevo')
                    elif opcion==2:
                        print(estudiantes)
                        eliminar=int(input('Eliminar\n1.Cédula\n2.Materia\n3.Nombre'))
                        if eliminar==1:
                            ci=input('Ingrese su cédula: ')
                            for i in s:
                                if ci==s[i]:
                                    s.pop(ci)
                                    print('Completado')
                                    print(estudiantes)
                                    dato=True
                                else:
                                    print(f'No existe la cédula {ci}, intente de nuevo')
                                    dato=False
                        elif eliminar==2:
                            materias_borrada=input('Ingrese su materia a eliminar: ').lower()
                            for i in s:
                                if materias_borrada==s[i]:
                                    s.pop(materias_borrada)
                                    print('Completado')
                                    print(estudiantes)
                                    dato=True
                                else:
                                    print('Dato incorrecto, inténtelo de nuevo')
                        elif eliminar==3:
                            nr=input('Ingrese su nombre registrado: ').lower()
                            for i in estudiantes:
                                if nr==estudiantes[i]:
                                    estudiantes.pop(nombre)
                                    print('Completado')
                                    print(estudiantes)
                                    dato=True
                        else:
                            print('Dato incorrecto, intenta de nuevo')
                    else:
                        print('Dato incorrecto, intente de nuevo')
                else:
                    print('Dato incorrecto, intente de nuevo')
            decision=print('Quieres continuar? (y o n): ').lower()
            if decision=='n':
                dato=True
                print('Sesión cerrada')
                abierto=True
            else:
                dato=False
        else:
            edad= int(input('Ingrese edad: '))
            cédula= int(input('Ingrese cédula '))
            n= int(input('Número de materias en curso: '))
            x=0
            while x<n:
                mat= input('Ingrese materia en curso: ').lower()
                materia.append(mat)
                x+=1
            s=[nombre, edad, cédula, materia]
            estudiantes.append(s)
            print(estudiantes)
            d=print('Usuario registrado\nDesea continuar? (y o n): ')
            if d==n:
                abierto=True
                print('Vuelva pronto')
            else:
                abierto=False


