usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []
# for i in usuarios:
#     nombres.append(i[0])
# print(nombres)

#var = [expresion for item in items]

#modificar (map)
nombres = [usuario[0] for usuario in usuarios]
print(nombres)
 
# filtrar (filter)
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)
 
# Map
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

#filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios ))
print(menosUsuarios)