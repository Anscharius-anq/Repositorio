print(round(1.3))  # salida: 1 ; redondea al entero más cercano y lo devuelve como entero
print(round(2.5))  # salida: 2 ; redondea a un numero par más cercano cuando el decimal es 0.5
print(round(3.5))  # salida: 4 ; redondea a un numero par más cercano cuando el decimal es 0.5

print(abs(-1))  # salida: 1 ; devuelve el valor absoluto de un número   



# Funciones de la libreria math (Python Math Library)
import math 

# lo mas impostante de la libreria math
print(math.ceil(1.1)) # salida: 2 ; redondea al entero más cercano hacia arriba
print(math.floor(1.9)) # salida: 1 ; redondea al entero más cercano hacia abajo

print(math.isnan(1)) # salida: False ; verifica si un valor es NaN (Not a Number)
print(math.isnan(float('23'))) # salida: True ; verifica si un valor es NaN (Not a Number)

print(math.pow(10, 3)) # salida: 1000.0 ; eleva un número a una potencia (float)
print(math.sqrt(9)) # salida: 3.0 ; devuelve la raíz cuadrada de un número (float)

