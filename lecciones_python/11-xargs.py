# *args: es un parametro se usa para pasar una cantidad variable de argumentos a una función
# *args: forma una tupla con los argumentos pasados a la función

def suma(*numeros):
    resultado = 0 
    print(type(numeros)) # <class 'tuple'>
    for numero in numeros: # es mejor usar sum(), pero bueno
        resultado += numero 
    print(resultado)

suma(3, 5, 6, 7) # se puede pasar cualquier cantidad de argumentos

