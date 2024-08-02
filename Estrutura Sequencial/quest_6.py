def main():
  print ('Calculadora de km/h para m/s')
  print ('---------------')
  
  kh = int(input('Qual valor deseja converter?: '))
  
  ms = int(kh / 3.6)
  
  print (f'{kh} Km/h são {ms} M/s')

main()
