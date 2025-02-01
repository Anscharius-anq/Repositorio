def calcular_promedio(*calificaciones):
    return sum(calificaciones) / len(calificaciones)

def clasificar_estudiante(media):
    match media:
        case media if media >= 90:
            rendimiento = "Excelente"
        case media if media >= 70 and media < 90:
            rendimiento = "Bueno"
        case media if media >= 50 and media < 70:
            rendimiento = "Regular"
        case media if media < 50:
            rendimiento = "Insuficiente"
    return rendimiento


# Introducción
print("=" * 64)
print("Bienvenido al programa de cálculo de promedios y clasificaciones.")
print("=" * 64)

# Validar entrada del usuario
while True:
    try:
        calificacion = input("\n>>> Ingresa las calificaciones del estudiante, separadas por comas: \n")
        tupla_int = tuple([int(s.strip()) for s in calificacion.split(",")])
        break
    except ValueError:
        print("Por favor, ingresa solo números separados por comas.")
print("=" * 64)

# Calcular promedio y clasificación
media = calcular_promedio(*tupla_int)
rend = clasificar_estudiante(media)

# Mostrar resultados
print(f"""\nPromedio del estudiante: {media:.2f}
Clasificación: {rend}\n""")
