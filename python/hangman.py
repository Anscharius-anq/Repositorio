import os
import sys
import random
import time


def remove_previous_line(times: int = 1):
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

    for _ in range(times):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def user_input():
    while True:
        try:
            user_letter = input("\n> Escriba una letra: ").strip().lower()

            if len(user_letter) != 1:
                print("Error: Ingrese una sola letra.")
                continue
            if not user_letter.isalpha():
                print("Error: Solo se permiten letras.")
                continue

            return user_letter

        except KeyboardInterrupt:
            print("\nEntrada Interrumpida. Saliendo del juego...")
            sys.exit(1)


def remove_accents(word: str, /) -> str:
    VOWELS = "aeiouuAEIOUU"
    ACCENTS = "áéíóúüÁÉÍÓÚÜ"

    # Diccionario para mapeo de acentos
    accent_map = {acc: vow.lower() for acc, vow in zip(ACCENTS, VOWELS)}

    # Normalización usando el diccionario
    return "".join(accent_map.get(char, char) for char in word)


def read_file(path_file):
    try:
        with open(path_file, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"No se encontró el archivo: {path_file}")
    except IOError:
        print(f"Ocurrió un error al leer el archivo: {path_file}")
    return None


def list_lines_file(path_file):
    file_content = read_file(path_file)
    if file_content is None:
        return []
    return [line.strip() for line in file_content.split("\n") if line.strip()]


def random_word(path_file):
    words = list_lines_file(path_file)
    if not words:  # Verifica si words está vacío
        print("El archivo no contiene palabras válidas.")
        return None
    return random.choice(words)


def print_status(empty_list, attempts, incorrect_letters):

    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ".join(empty_list))
    print()
    print(f"· Intentos restantes: {attempts}")
    print(f"· Letras incorrectas: {", ".join(incorrect_letters).upper()}")


def restart_game():
    while True:
        player_choice = input(
            "> ¿Deseas comenzar otra partida? [S/n]: ").lower()

        match player_choice:
            case "s" | "si" | "sí" | "y" | "yes":
                return True
            case "n" | "no":
                return False
            case _:
                remove_previous_line()
                print("Entrada no válida.")
                continue


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        path_file = "python/hangman_words.txt"
        word = random_word(path_file)
        normalized_word = remove_accents(word)

        empty_list = ["_"] * len(word)
        attempts = 6
        incorrect_letters = []

        while True:
            print_status(empty_list, attempts, incorrect_letters)

            user_letter = user_input()

            if user_letter in normalized_word:
                for index in range(0, len(normalized_word)):
                    if normalized_word[index] == user_letter:
                        empty_list[index] = user_letter

                if not "_" in empty_list:
                    print_status(empty_list, attempts, incorrect_letters)
                    print(f"¡Has ganado! La palabra correcta es {word}.")
            else:
                if user_letter in incorrect_letters:
                    print("Ya has escrito esta letra.x")
                    continue

                attempts -= 1
                incorrect_letters.append(user_letter)
                print("\nletra equivocada")

                if attempts == 0:
                    print("Te has quedado sin intentos.",
                          f"la palabra correcta es: {word.capitalize()}")
                    break
            
        if not restart_game():
            break
        


        print("\n--- Fin del juego ---\n")


if __name__ == "__main__":
    main()
