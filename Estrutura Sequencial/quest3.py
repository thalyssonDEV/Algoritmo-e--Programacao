def main():
  print('Transformar Minutos em Horas/Minutos')
  print('-------------')
  
  mn = int(input('Qual valor em Minutos?: '))
  print('--------------')
  
  resultado_horas = int(mn / 60)
  resultado_min = mn % 60
  
  print(f'Resultado = {resultado_horas} Horas e {resultado_min} Minutos!')

main()
