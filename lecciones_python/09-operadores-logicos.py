# los operadores logicos son:
    # and: y (ambas condiciones deben ser verdaderas) 
    # or: o (al menos una de las condiciones debe ser verdadera
    # not: negacion (cambia el valor de verdad de una condicion)

gas = True
encendido = True
edad = 18

# se ejecuta de izquierda a derecha, 
# por lo que si la primera condicion es falsa, no se evalua la segunda
# a la derecha se deja la mas pesada
if not gas and encendido and edad > 17:
    print("puedes avanzar")
