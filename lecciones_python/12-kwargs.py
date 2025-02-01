def get_product(**datos):
    print(datos)
    print(datos["id"], datos["name"])

# **kwargs: es un parametro se usa para pasar una cantidad variable de
    # argumentos a una función, pero en forma de diccionario, es decir,
    # clave: valor, por eso se llama keyword arguments.


get_product(id="23",
            name="nombre",
            price=1000,
            stock=10)
