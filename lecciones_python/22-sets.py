# set es conjuntos en ingles

primer = {1, 1, 2, 2, 3, 4}
print(primer)

primer.add(5)
primer.remove(1)
print(primer)

primer = {1, 2, 3, 4}
segundo = [3, 4, 5, 6, 7]
segundo = set(segundo)
print(segundo)

print(primer | segundo)  # union
print(primer & segundo)  # interseccion
print(primer - segundo)  # diferencia
print(primer ^ segundo)  # diferencia simetrica

# no se puede acceder a un elemento de set, pero podemos hacer:
if 5 in segundo:
    print("se encuentra el 5")
