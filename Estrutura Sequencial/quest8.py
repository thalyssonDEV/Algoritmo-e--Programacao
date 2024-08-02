def main():
  print('Divisão da soma pela subtração de um Número')
  print('-----------')
  
  numA = int(input('Digite um Número: '))
  numB = int(input('Digite outro Número: '))
  
  resultado = (numA + numB) / (numA - numB)
  
  print('------------')
  print(f'A divisão da soma pela subtração dos algarismos é {resultado}!')

main()
