def main():
  print('Calcular 70% de um valor em Real (R$)')
  print('------')
  
  real = float(input('Digite o valor: '))
  
  resultado = real * 7/10
  
  print('------')
  print(f'70% de {real:.2f} é igual a {resultado:.2f} Reais')

main()
