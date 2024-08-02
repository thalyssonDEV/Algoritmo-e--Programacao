def main():
  print('Inventer um número inteiro de 3 dígitos')
  print('---------')
  
  num = int(input('Digite o Número: '))
  print('---------')
  
  alg1 = num // 100
  alg2 = num % 100 // 10
  alg3 = num % 10
  
  print(f'A inversão do seu número é {alg3}{alg2}{alg1}!')

main()
