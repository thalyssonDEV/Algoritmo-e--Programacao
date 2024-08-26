import os
import random
import sys
import time


def wait_press_enter():

  input(color("PRESS ENTER", "laranja"))


def clean_screen():

  os.system("cls") if os.name == "nt" else os.system("clear")


def print_slow(text,delay = 0.015):
  
  for char in text:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(delay)
  print()


def color(array,codigo_cor):
  
  array_codigos = {
      "vermelho": 31,
      "verde_claro": 32,
      "laranja": 33,
      "azul_escuro": 34,
      "roxo": 35,
      "azul_claro": 36
  }
  color = array_codigos.get(codigo_cor)

  new_array = "\033[" + str(color) + "m" + array + "\033[m"

  return new_array


def get_random_vector(tamanho,minimo,maximo):
  
  vetor = []
  for _ in range(tamanho):
    vetor.append(random.randint(minimo,maximo))

  return vetor
  

def sum_values(vetor_atual):
 
  soma_total = 0
  for char in vetor_atual:
    soma_total += char

  return soma_total


def get_media(vetor_atual):
  
  soma_total = 0
  qtd_char = 0
  for char in vetor_atual:
    soma_total += char
    qtd_char += 1

  return (soma_total / qtd_char)


def get_posivites_negatives(parameter,vetor_atual):
 
  match parameter:
    case 1:
      vetor_negativos = []
      for char in vetor_atual:
        if char < 0:
          vetor_negativos.append(char)

      return vetor_negativos
    
    case 2:
      vetor_positivos = []
      for char in vetor_atual:
        if char > 0:
          vetor_positivos.append(char)

      return vetor_positivos


def multiply_vector(vetor_atual,valor):
  
  vetor_multiplicado = []
  for char in vetor_atual:
    vetor_multiplicado.append(char * valor)

  return vetor_multiplicado


def elevate_vector(valor,vetor_atual):
  
  vetor_elevado = []
  for char in vetor_atual:
    for _ in range(valor-1):
      char *= char
    vetor_elevado.append(char)

  return vetor_elevado


def replace_vector_negative(min,max,vetor_atual):
  
  index = 0
  for char in vetor_atual:
    if char < 0:
      vetor_atual[index] = random.randint(min,max)
    
    index += 1

  return vetor_atual


def sort_vector(vetor_atual):

  for z in range(len(vetor_atual)):
    for z in range(len(vetor_atual)-1):
      if vetor_atual[z] > vetor_atual[z + 1]:

        maior = vetor_atual[z]
        vetor_atual[z] = vetor_atual[z + 1]
        vetor_atual[z + 1] = maior

  return vetor_atual


def shuffle_vector(vetor_atual):
    
  for i in range(len(vetor_atual) - 1, 0, -1):
        j = random.randint(0, i)
        vetor_atual[i], vetor_atual[j] = vetor_atual[j], vetor_atual[i]
    
  return vetor_atual


def division_vector(vetor_atual,numerador,denominador):
  
  vetor_dividido = []
  for char in vetor_atual:
    valor_arredondado = round((char * numerador) / denominador, 1)
    vetor_dividido.append(valor_arredondado)

  return vetor_dividido


def add_to_vector(qtd_valores,vetor_atual):
  
  posicao = 1
  for _ in range(qtd_valores):
    valor_novo = int(input(color(f"Valor {posicao}: ","azul_claro")))
    vetor_atual.append(valor_novo)
    posicao += 1

  return vetor_atual


def reset_vector(vetor_atual,valor_padrao):
  
  vetor_resetado = []
  for _ in range(len(vetor_atual)):
    vetor_resetado.append(valor_padrao)

  return vetor_resetado


def remover_exact_value(qtd_num_removidos,vetor_atual):

  posicao = 1
  lista_removidos = []
  vetor_novo = []
  for _ in range(qtd_num_removidos):
    valor_removido = float(input(color(f"{posicao}º Valor Removido: ","azul_claro")))
    lista_removidos.append(valor_removido)
    posicao += 1

  for item in vetor_atual:
    if item not in lista_removidos:
      vetor_novo.append(item)

  return vetor_novo


def remove_by_position(qtd_num_removidos,vetor_atual):

  posicao = 1
  lista_removidos = []
  vetor_novo = []
  for _ in range(qtd_num_removidos):
    posicao_removida = int(input(color(f"Posição do {posicao}º Valor Removido: ","azul_claro")))
    lista_removidos.append(vetor_atual[posicao_removida-1])
    posicao += 1

  for item in vetor_atual:
    if item not in lista_removidos:
      vetor_novo.append(item)

  return vetor_novo


def edit_value_by_position(vetor_atual,posicao_editada,valor_novo):
  
  vetor_atual[posicao_editada-1] = valor_novo

  return vetor_atual


def save_file(vetor_atual,nome_arquivo):
  
  with open(f'{nome_arquivo}.txt', 'w') as arquivo:
    for item in vetor_atual:
      arquivo.write(f"{item}\n")

def lowercase_name(name):
  
  new_name = ""
  for char in name:
    if "A" <= char <= "Z":
      new_name += chr(ord(char) + 32)
    else:
      new_name += char
  new_name += "_vetor"

  return new_name


def get_min_and_max(vetor_atual):

  maior = menor = vetor_atual[0]
  for char in vetor_atual:
    if char > maior:
      maior = char
    
    if char < menor:
      menor = char

  return menor,maior


def get_position_numbers(menor,maior,vetor_atual): ## ARRUMAR

  posicao_maior = 1
  for char in vetor_atual:
    if char != maior:
      posicao_maior += 1
    else:
      break

  posicao_menor = 1
  for char in vetor_atual:
    if char != menor:
      posicao_menor += 1
    else:
      break

  return posicao_menor,posicao_maior
  
# def progress_bar(percentual, largura=40, mensagem="SALVANDO"):
  
#   preenchido = int(percentual / 100 * largura)
#   barra = '█' * preenchido + '░' * (largura - preenchido)

#   animacao_reticencias = ['.', '..', '...']
#   animacao = animacao_reticencias[int((percentual / 100) * len(animacao_reticencias)) % len(animacao_reticencias)]

#   progresso = f'\r[{barra}] {mensagem} {percentual:.0f}% {animacao}'
#   sys.stdout.write(progresso)
#   sys.stdout.flush()


# def loading_simulator(tempo_total=3, largura_barra=50):
  
#   intervalos = 100
#   intervalo_tempo = tempo_total / intervalos

#   for i in range(intervalos + 1):
#       percentual = i
#       progress_bar(percentual, largura_barra)
#       time.sleep(intervalo_tempo)
#   print()
