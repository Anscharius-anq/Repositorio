#alcance (scope) de las variables
saludo = "Saludo Global"

def saludar():
    saludo = "Hola Mundo"
    print(saludo)

def saludachachito():
    saludo = "Hola Chachito"
    print(saludo)


# saludo tiene alcance local a la funciones
# por lo tanto, saludo no existe fuera de las funciones saludar y saludachachito
# print(saludo) # NameError: name 'saludo' is not defined

saludar() # Hola Mundo
saludachachito() # Hola Chachito
print(saludo) # Saludo Global

# las variables saludo de ambas funciones son completamente distintas

# las variables que normalmente se declaran fuera de las funciones
# tienen alcance global, es decir, pueden ser accedidas desde cualquier 
# parte del programa.

# el uso de variables globales no es recomendado, ya que puede llevar a
# errores en el programa, es mejor usar variables locales y pasarlas
# como argumentos a las funciones que las necesiten.

# entonces, el uso de variables globales es una mala práctica de programación.

# pero si por alguna razón necesitas usar variables globales, puedes hacerlo
# usando la palabra reservada global seguida del nombre de la variable.
# dentro de la función que la necesite.

def saludar_global():
    global saludo
    saludo = "Hola Mundo"
    print(saludo)