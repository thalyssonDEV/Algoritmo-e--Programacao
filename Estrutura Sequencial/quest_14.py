def main():
  print('Calculadora de Média Ponderada')
  print('-------')
  
  nt1 = float(input('Qual sua nota 1? : '))
  p1 = float(input('Qual o peso da nota 1? : '))
  print('-------')
  nt2 = float(input('Qual sua nota 2? : '))
  p2 = float(input('Qual o peso da nota 2? : '))
  print('-------')
  nt3 = float(input('Qual sua nota 3? : '))
  p3 = float(input('Qual o peso da nota 3? : '))
  
  soma_notas = ( nt1 * p1 ) + ( nt2 * p2 ) + ( nt3 * p3 )
  soma_pesos = (p1 + p2 + p3 )
  media_pond = soma_notas / soma_pesos
  
  print('------')
  print(f'Sua média é {media_pond:.1f}!')

main()
