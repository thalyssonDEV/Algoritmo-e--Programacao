def main():
  print('Divisão e Resto de um número inteiro ')
  print('--------')
  
  num1 = int(input('Digite o 1° Número: '))
  num2 = int(input('Digite o 2° Número: '))
  
  quociente = int(num1 / num2)
  resto = (num1 % num2)
  
  print('---------')
  print(f'A divisão do 1° Número pelo 2° é {quociente}')
  print('_________')
  print(f'O resto da divisão do 1° Número pelo 2° é {resto}')

main()
