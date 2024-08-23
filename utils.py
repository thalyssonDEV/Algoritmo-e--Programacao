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

def wait_press_enter():
  input(color("PRESS ENTER",36))

def sum_values(vetor_atual):
  soma_total = 0
  for char in vetor_atual:
    soma_total += char

  return soma_total
