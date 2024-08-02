def main():
  print ('Conversor de Horas e Minutos')
  print ('------------')
  
  hr = float(input('Valor em Horas: '))
  mn = float(input('Valor em Minutos: '))
  print ('---------------')
  
  mn2 = hr * 60
  resultado = mn2 + mn
  
  print (f'O resultado é {resultado} Minutos!')

main()
