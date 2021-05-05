#Número par/impar
#Número positivo/negativo

x= input('Ingrese un número: ')

if not x.isalpha():
    x=int(x)
    if x%2==0:
        if x>=0:
            print(f'El número {x} es par y positivo')
        else:
            print(f'El número {x} es par y negativo')
    else:
        if x>=0:
            print(f'El número {x} es impar y positivo')
        else:
            print(f'El número {x} es impar y negativo')
else:
    print('Dato incorrecto')
