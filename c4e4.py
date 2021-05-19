#Debe escribir un While Loop que tome los números en una lista dada llamada: num_list
#Su código debe sumar los números impares en la lista, pero solo hasta los primeros 5 números impares.
#Sumar los primeros 5 números impares en la lista.
#Si hay mas de 5 números impares, detenerse de sumar en el 5to número y mostrar mensaje con la cantidad de números impares y la suma total.

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69 , 113, 166]
num_impares = []
suma_impares = []

i=0
while i < len(num_list):
    if (num_list[i]%2)==1:
        num_impares.append(num_list[i])
    i+=1

contador_impares = len(set(num_impares))

for j in range(6):
    suma_impares.append(num_impares[j])

print(f'La cantidad de números impares es: {contador_impares} y la suma es: {sum(set(suma_impares))}')
