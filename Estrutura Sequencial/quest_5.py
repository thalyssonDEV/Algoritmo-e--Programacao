def main():
  print('Soma de elementos de um número inteiro de 3 dígitos')
  print('-----------')
  
  numero = int(input('Digite o número: '))
  
  alg_1 = int(numero / 100)
  alg_2 = int(numero % 100 / 10)
  alg_3 = int(numero % 10 )
  
  print('------------')
  resultado = alg_1 + alg_2 + alg_3 
  print(f'Resultado = {resultado}')

main()
