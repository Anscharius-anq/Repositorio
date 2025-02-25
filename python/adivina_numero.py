import random
import time
import os
import sys


def user_input(start: int, end: int) -> int:
    """Solicita un número al usuario dentro de un rango especificado."""
    while True:
        try:
            user_number = int(
                input(f"> Ingrese un número entre [{start} - {end}]: "))
            if start <= user_number <= end:
                return user_number
            else:
                print(f"El número debe estar entre {start} y {end}.")
        except ValueError:
            print("Error: Ingrese un número válido.")
        except KeyboardInterrupt:
            print("\n Cierre forzado. Saliendo del programa...")
            sys.exit(0)


def waiting_animation():
    frame_animation = ["   ", ".  ", ".. ", "...", "   "]

    for frame in frame_animation:
        print(f"{frame}\r", end="")
        time.sleep(0.1)


def restart():
    while True:

        restart_confirmation = input(
            "¿Desea comenzar otra ronda? [S/n]: ").strip().lower()

        match restart_confirmation:
            case "s" | "si" | "sí" | "yes" | "y":
                return True
            case "no" | "n":
                return False
            case _:
                print("Error: Entrada no reconocida . Por favor, ingrese 'S' o 'N'.")


def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    start, end = 0, 100

    print("--- ¡Bienvenido al juego de adivinar un número! ---")
    print("He pensado un número, ¡intenta adivinarlo!")

    while True:

        generated_number = random.randint(start, end)
        attempts = 0

        while True:

            attempts += 1
            number = user_input(start, end)
            waiting_animation()

            if generated_number == number:
                print(
                    f"¡Correcto! El número es {number}. Lo lograste en {attempts} intentos.")
                break
            elif generated_number < number:
                print(
                    f"Incorrecto. Intento: {attempts}, el número es menor a {number}")
            elif generated_number > number:
                print(
                    f"Incorrecto. Intento: {attempts}, el número es mayor a {number}")

        if not restart():
            print("--- Fin del programa ---")
            break

        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
