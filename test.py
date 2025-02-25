import os
import random
import sys
import time


def hangman_animation(frame):
    with open("C:/Users/oscar/workspace/repositorio/python/hangman_frames.txt",
              "r", encoding="utf-8") as file:
        hangman_ascii = file.read()

    animation = hangman_ascii.split("\n\n")
    return animation[frame]


def show_blink_effect(frame):

    def clear_previous_frame():
        CURSOR_UP_ONE = '\x1b[1A'
        ERASE_LINE = '\x1b[2K'

        for _ in range(7):
            sys.stdout.write(CURSOR_UP_ONE)
            sys.stdout.write(ERASE_LINE)

    actual_frame = hangman_animation(frame)
    next_frame = hangman_animation(frame + 1)

    for _ in range(3):
        print(actual_frame)
        time.sleep(0.3)
        clear_previous_frame()
        print(next_frame)
        time.sleep(0.3)
        clear_previous_frame()

    print(next_frame)
    time.sleep(0.3)


def main():

    print("bienvenida")
    for i in range(6):
        show_blink_effect(i)
    print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
