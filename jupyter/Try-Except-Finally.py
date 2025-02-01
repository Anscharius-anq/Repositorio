''''
Los bloques try, except  sirven para realizar ciertas acciones en caso de que ocurran fallos y especificar 
que acciones realizar en caso de ocurrir.
'''

def dividir(dividendo, divisor):
    try:
        # intentamos realizar una division
        resultado = round(dividendo/divisor, 2)
        print(resultado) 
    except ZeroDivisionError:
        # En el caso de que se produzca una excepción ZeroDivisionError, mostramos un mensaje de error.
        print("No se puede dividir por cero,")
    except TypeError:
        print("valor no aceptado.")
    finally:
        # mostramos un mensaje de finalización
        print("La operación ha finalizado")


dividir(10,0)