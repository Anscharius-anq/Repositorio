numeros = [2, 4, 1, 45, 75, 22]


# numeros.sort() # ordena los elementos
numeros.sort(reverse=True) # reordena alreves un iterable
numeros2 = sorted(numeros) # crea un nuevo listado ordenado, osea la lista original esta intacta
 
print(numeros)
print(numeros2)


usuarios = [
    [4, "Chanchito"], 
    [1, "Felipe"], 
    [5, "Pulga"]
]

usuarios.sort()
print(usuarios)



usuarios = [
    ["Chanchito", 4], 
    ["Felipe", 1], 
    ["Pulga", 5]
]

# def ordena(elemento):
#    return elemento[1]
# usuarios.sort(key=ordena)

# mejor usar:
usuarios.sort(key=lambda elemento:elemento[1])
print(usuarios)

