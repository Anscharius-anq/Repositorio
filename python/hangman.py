import os
import sys
import random
import time


def remove_previous_lines(times: int = 1):
    CURSOR_UP_ONE = "\x1b[1A"
    ERASE_LINE = "\x1b[2K"

    for _ in range(times):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def hangman_ascii_file():
    with open(
        "./documents/hangman_frames.txt",
        "r",
        encoding="utf-8",
    ) as file:
        return file.read()


def hangman_frames(frame):
    animation = hangman_ascii_file().split("\n\n")
    return animation[frame]


def user_input():
    while True:
        try:
            user_letter = input("\n> Escriba una letra: ").strip().lower()
            remove_previous_lines(2)

            if user_letter.isalpha() and len(user_letter) == 1:
                return user_letter
            elif user_letter.isnumeric():
                print("Error: Solo se permiten letras.")
                continue
            elif len(user_letter) == 0:
                print("Error: Ingrese alguna letra")
                continue
            elif len(user_letter) != 1:
                print("Error: Ingrese una sola letra.")
                continue
            else:
                print("Error: Escriba un carácter válido.")
                continue

        except KeyboardInterrupt:
            print(f"\nKeyboardInterrupt: Forzando cierre")
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


def get_user_confirmation(message: str) -> bool:
    while True:
        player_choice = input(f"> {message} [S/n]: ").lower()
        remove_previous_lines()

        match player_choice:
            case "s" | "si" | "sí" | "y" | "yes":
                return True
            case "n" | "no":
                return False
            case _:
                print("Entrada no válida.")
                continue


def display_animation(frame):

    for _ in range(2):
        print(hangman_frames(frame))
        time.sleep(0.3)
        remove_previous_lines(7)

        print(hangman_frames(frame - 1))
        time.sleep(0.3)
        remove_previous_lines(7)


def print_status(empty_list, attempts, incorrect_letters, message):

    os.system("cls" if os.name == "nt" else "clear")
    print(hangman_frames(attempts))
    print()
    print(" ".join(empty_list))
    print()
    print(f"· Letras incorrectas: {", ".join(incorrect_letters).upper()}" if attempts !=0 else " ")
    print(message)


def main():
    os.system("cls" if os.name == "nt" else "else")
    print("!Bienvenido al juego del ahorcado!")
    time.sleep(1)
    if not get_user_confirmation("¿desea iniciar una partida?"):
        print("cerrando juego.")
        sys.exit(1)

    interface = lambda: print_status(empty_list, attempts, incorrect_letters, message)

    while True:

        os.system("cls" if os.name == "nt" else "clear")

        path_file = "documents/hangman_words.txt"
        word = random_word(path_file)
        normalized_word = remove_accents(word)

        empty_list = ["_"] * len(word)
        attempts = 0
        incorrect_letters = []
        message = ""

        while True:
            interface()
            user_letter = user_input()

            if user_letter in (empty_list or incorrect_letters):
                message = f"Ya has escrito la letra {user_letter.upper()}."
                continue

            # caso correcto
            if user_letter in normalized_word:
                for index in range(0, len(normalized_word)):
                    if normalized_word[index] == user_letter:
                        empty_list[index] = user_letter
                        interface()

                if not "_" in empty_list:
                    message = f"¡Has ganado! La palabra correcta es {word}."
                    interface()
                    break
            # caso incorrecto
            else:
                if user_letter in incorrect_letters:
                    message = f"Ya has escrito la letra {user_letter.upper()}."
                    interface()
                    continue

                attempts += 1
                incorrect_letters.append(user_letter)
                message = "Letra incorrecta"
                for _ in range(2):
                    print_status(empty_list, attempts, incorrect_letters, message)
                    time.sleep(0.3)

                    print_status(empty_list, attempts - 1, incorrect_letters, message)
                    time.sleep(0.3)
                else:
                    print_status(empty_list, attempts, incorrect_letters, message)

                if attempts >= 6:
                    interface()
                    print(
                        "Te has quedado sin intentos.",
                        f"La palabra correcta es: {word.capitalize()}",
                    )
                    break

        time.sleep(1)
        print()
        if not get_user_confirmation("¿Desea comenzar una nueva partida?"):
            break

    print("--- Fin del programa ---")
    print()


if __name__ == "__main__":
    main()
