'''el objetivo es calcular la longitud o la cantidad 
de caracteres que tiene un texto, es decir, un len()'''


def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print("chanchito")
l = largo("Hola mundo")
print(l)  # 10
