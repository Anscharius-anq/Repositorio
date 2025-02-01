
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("un año más y serás mayor de edad")
else:
    print("Eres menor de edad")

print("Fin del programa")

#operador ternario
    # Es una forma de simplificar un if else       
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"