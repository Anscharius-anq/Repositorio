# Para utilizr los elementos de una lista como variables independientes
# se podria realizar lo siguiente:

numeros = [1, 2, 3]

# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# sin embargo, es la peor manera que puedes hacer esto
# una mejor manera es lo siguiente:

# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

# si queremos asignar una variable a un elemento de la lista nos da error:
# primero, = numeros

# pero si se puede usar * par desempaquerar los elementos restantes
# primero, *otros = numeros
# print(primero, otros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

primero, segundo, *otros, penultimo, ultimo = numeros
print(primero, segundo, otros, penultimo, ultimo)
B