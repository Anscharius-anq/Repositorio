animal = "chAnCHiTo fEliz  "

print("1. ", animal)
print("2. ", animal.upper())  # convierte todo a mayusculas
print("3. ", animal.lower())  # convierte todo a minusculas
print("4. ", animal.capitalize())  # convierte la primera letra a mayuscula
print("5. ", animal.title()) # convierte la primera letra de cada palabra a mayuscula
print("6. ", animal.swapcase()) # convierte mayusculas en minusculas y viceversa
print("7. ", animal.strip())  # elimina espacios en blanco al inicio y al final
print("8. ", animal.lstrip()) # elimina espacios en blanco al inicio (left)
print("9. ", animal.rstrip()) # elimina espacios en blanco al final (right)
print("10. ", animal.find("CH"))  # busca la subcadena y devuelve la posicion de la primera ocurrencia
print("11. ", animal.find("cH")) # si no encuentra la subcadena, devuelve -1   
print("12. ", animal.replace("nCH", "j"))  # reemplaza la subcadena por otra
print("13. ", animal.split())  # divide la cadena en una lista de palabras (por defecto, separa por espacios)
print("14. ", animal.split("n"))  # al especificar el separador, divide la cadena en una lista de palabras

print("15. ", "nCH" in animal)  # verifica si la subcadena esta en la cadena(True/False)
print("16. ", "nCH" not in animal)  # verifica si la subcadena no esta en la cadena(True/False)

# estos metodos no modifican la cadena original (inmutabilidad), sino que devuelven una nueva cadena
