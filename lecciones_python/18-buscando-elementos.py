mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito"]

# para buscar un elementos de un listado, siempre y cuando exista
print(mascotas.index("Pulga"))

# si no existe en muschos lenguajes devuelve -1 pero en python arroja error
# asi que para resulver podemos
if "Wolfgang" in mascotas:
    print(mascotas.index("Wolfgang"))  # no imprime por que no existe


# ________________________


mascotas = ["Pelusa", "Wolfgang", "Felipe", "Wolfgang", "Chanchito"]


print(mascotas.count("Wolfgang"))
if "Wolfgang" in mascotas:
    print(mascotas.index("Wolfgang"))
