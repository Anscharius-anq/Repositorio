mascotas = ["pelusa", "Pulga", "Felipe", "Chanchito"]

#no muestra los elementos de la lista
for mascota in mascotas:
    print(mascota)

# enumerate es un devuelve un iterable con los indices y los elementos de la lista
# en forma de tuplas (indice, elemento)
# indice, mascota desempaqueta la tupla
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)