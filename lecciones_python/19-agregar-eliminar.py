mascotas = ["Wolfgang",
            "Pelusa",
            "Pulga",
            "Felipe",
            "Pulga"
            "Chanchito"
            ]


mascotas.insert(1, "Melvin")# inserta "Melvin" a la posicion 1, moviendo una posicion a todos los que estaban por delante
mascotas.append("Chancho")  # añade el nuevo elemento al final del listado

mascotas.remove("Pulga") # elimina la primera ocurencia 
mascotas.pop() # elimina el ultimo elemento
mascotas.pop(1) # elimina al elemento del indice indicado
del mascotas[0] 
mascotas.clear() # entrega un listado vacio

print(mascotas)
