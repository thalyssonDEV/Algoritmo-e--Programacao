from cores import GREEN,BOLD,YELLOW,BLUE,MAGENTA,RESET,CYAN,RED,LIGHT_BLUE,LIGHT_YELLOW
 
## FISHER-YATES
explicacao_fisher_yates = f"""
  {GREEN}{BOLD}A Mágica do Embaralhamento: Algoritmo de Fisher-Yates{RESET}

  {MAGENTA}Imagine um Baralho de Cartas Ordenadas. Uma Ótima Alternativa para Embaralhar é o Algoritmo de Fisher-Yates!{RESET}

  {YELLOW}{BOLD}Lógica do Algoritmo no Baralho:{RESET}

  1. {LIGHT_BLUE}Escolha uma Posição Aleatória para a Carta da sua Posição Atual.{RESET}
  2. {LIGHT_BLUE}Troque a Carta Atual com a Carta da Posição Escolhida.{RESET}
  3. {LIGHT_BLUE}Repita para Todas as Cartas.{RESET}

  {YELLOW}{BOLD}Implementação no Código:{RESET}

  1. {LIGHT_BLUE}Começamos do Final da Lista e é Escolhida uma Posição Aleatória para cada Valor.{RESET}
  2. {LIGHT_BLUE}Trocamos o Valor Atual com o Valor da Posição Escolhida.{RESET}
  3. {LIGHT_BLUE}Repetimos até que Todos os Valores Tenham sido Embaralhados.{RESET}

  {MAGENTA}Por Que o Algoritmo é Eficiente?{RESET} {BOLD}Cada Possível Ordenação das Cartas têm a Mesma Probabilidade!{RESET}

  {CYAN}Dessa Forma, Temos:{RESET} {BOLD}Uma Mistura Justa e Aleatória dos Elementos do Vetor!{RESET}

  {BOLD}===================|||||||||======================={RESET}
  
  {RED}{BOLD}Código do Algoritmo Fisher-Yates:{RESET}

    import {BLUE}random{RESET}

    {BLUE}def {LIGHT_YELLOW}shuffle_vector{RESET}(vector):
      {BLUE}for{RESET} i {BLUE}in{RESET} {LIGHT_YELLOW}range{RESET}({LIGHT_YELLOW}len{RESET}(vector) {LIGHT_BLUE}-{RESET} {GREEN}1{RESET}, {GREEN}0{RESET}, {LIGHT_BLUE}-{RESET}{GREEN}1{RESET}): 
        j {LIGHT_BLUE}={RESET} random.{LIGHT_YELLOW}randint{RESET}(0, i)  
        vector[i], vector[j] {LIGHT_BLUE}={RESET} vector[j], vector[i]

      {BLUE}return{RESET} vector
"""

## BUBBLE SORT
explicacao_bubble_sort = f"""
  {GREEN}{BOLD}O Segredo da Ordenação: Algoritmo Bubble Sort{RESET}

  {MAGENTA}Imagine um Baralho de Cartas Numéricas Desorganizado, Uma Boa Alternativa para Ordenar é o Algoritmo Bubble Sort!{RESET}

  {YELLOW}{BOLD}Lógica do Algoritmo no Baralho:{RESET}

  1. {LIGHT_BLUE}Compare Cada Par de Elementos Adjacentes.{RESET}
  2. {LIGHT_BLUE}Troque-os se Estiverem na Ordem Errada.{RESET}
  3. {LIGHT_BLUE}Repita até que Todos os Elementos Estejam na Ordem Correta.{RESET}

  {YELLOW}{BOLD}Implementação no Código:{RESET}

  1. {LIGHT_BLUE}Começamos do Início da Lista e Comparamos cada Elemento com o Próximo.{RESET}
  2. {LIGHT_BLUE}Se o Elemento Atual for Maior que o Próximo, Trocamos Eles.{RESET}
  3. {LIGHT_BLUE}Repetimos o Processo até que Nenhum Elemento Precise Mais ser Trocado.{RESET}

  {MAGENTA}Por Que o Algoritmo é Eficiente?{RESET} {BOLD}É Uma Forma Amigável e Simples de Ordenar Elementos, Embora Não Seja a Mais Rápida para Listas Grandes!{RESET}

  {CYAN}Dessa Forma, Temos:{RESET} {BOLD}Uma Ordenação Simples e Eficiente dos Elementos no Vetor!{RESET}
  
  {BOLD}===================|||||||||======================={RESET}

  {RED}{BOLD}Código do Algoritmo Bubble Sort:{RESET}

    {BLUE}def{RESET} {LIGHT_YELLOW}sort_vector{RESET}(vector):
      {BLUE}for{RESET} z {BLUE}in{RESET} {LIGHT_YELLOW}range{RESET}({LIGHT_YELLOW}len{RESET}(vector)):
        {BLUE}for{RESET} z {BLUE}in{RESET} {LIGHT_YELLOW}range{RESET}({LIGHT_YELLOW}len{RESET}(vector){LIGHT_BLUE}-{RESET}{GREEN}1{RESET}):
          {BLUE}if{RESET} vector[z] {LIGHT_BLUE}>{RESET} vector[z {LIGHT_BLUE}+{RESET} {GREEN}1{RESET}]:
    
            maior {LIGHT_BLUE}={RESET} vector[z]
            vector[z] {LIGHT_BLUE}={RESET} vector[z {LIGHT_BLUE}+{RESET} {GREEN}1{RESET}]
            vector[z {LIGHT_BLUE}+{RESET} {GREEN}1{RESET}] {LIGHT_BLUE}={RESET} maior
    
      {BLUE}return{RESET} vector
"""
