def color(array,codigo_cor):
    new_array = "\033[" + str(codigo_cor) + "m" + array + "\033[m" 

    return new_array

def get_random_vector(tamanho,minimo,maximo):
    from random import randint

    vetor = []
    for _ in range(tamanho):
        vetor.append(randint(minimo,maximo))
    
    return vetor

def clean_screen():
    import os

    os.system("cls") if os.name == "nt" else os.system("clear")

def slow_text(array):
    import time
    import sys

    atraso = 0.025
    for letra in array:
        sys.stdout.write(letra)  # Escreve a letra no terminal
        sys.stdout.flush()  # Garante que a letra seja exibida imediatamente
        time.sleep(atraso)  # Espera o tempo especificado
    print()  # Move para a próxima linha após o texto


def wait_press_enter():
    input(color("PRESS ENTER",33))
