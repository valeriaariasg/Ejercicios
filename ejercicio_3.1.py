# Realiza un programa que, dado un número entero positivo ingresado por teclado,
# imprima la suma de los números que lo componen. Si el valor de la suma es menor que 10,
# la respuesta es el valor obtenido, si no, es la suma de los dígitos de la suma de los dígitos.
# Por ejemplo: para 7 es 7, para 12 es 3, y para 845 es 8 (8+4+5 = 17 => 1+7 = 8).



n = input('Ingrese un número positivo: ')

while not n.isnumeric() or int(n)<1:
    n = input('Ingreso inválido. Ingrese un número positivo: ')

while int(n)>=10:
    suma=0
    for caracter in str(n):
        suma += int(caracter)
    n=suma
print(n)
