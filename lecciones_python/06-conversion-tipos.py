# input() devuelve un string


#funcion para convertir un string a un entero
# str() convierte un número a un string
# int() convierte un string a un entero
# float() convierte un string a un flotante
# bool() convierte un número a un booleano
    # convertil bool se evualua si el valor es falsy o truthy
    # falsy values: 0, 0.0, '', False, [], {}, None
    # truthy values: cualquier otro valor

print(bool("")) # salida: False ; un string vacío es falsy
print(bool("0")) # salida: True ; cualquier string es truthy
print(bool("False")) # salida: True ; cualquier string es truthy
print(bool(0)) # salida: False ; el número 0 es falsy
