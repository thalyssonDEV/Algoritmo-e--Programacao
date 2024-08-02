def main():
  print('Aumento de Salário ')
  print('---------')
  
  salario_atual = float(input('Digite o seu salário atual: '))
  print('----------')
  
  aumento = salario_atual * 1/4
  salario_novo = salario_atual + aumento
  
  print(f'Seu novo salário é {salario_novo:.2f} Reais, aproveite!')

main()
