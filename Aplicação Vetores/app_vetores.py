import vetores_funcionalidades as utils
import vetores_documentacao as docs
from cores import BLUE, BOLD, CYAN, LIGHT_GREEN, LIGHT_YELLOW, MAGENTA, RESET, YELLOW


def menu_leitura_arquivo():
    print(f"""\n{MAGENTA}===== SELECIONE O MODO EM QUE O VETOR SERÁ INICIALIZADO ==========={RESET}
[ 1 ] VETOR ALEATÓRIO
[ 2 ] ADICIONAR VALORES MANUALMENTE
[ 3 ] LER DE UM ARQUIVO""")


def menu_documentacao():
    print(f"""\n[ 1 ] Algoritmo de Ordenação
[ 2 ] Algoritmo de Embaralhamento
{BOLD}[ 0 ] Sair{RESET}""")


def menu_regras():
    print(f"""{MAGENTA}======= SELECIONE A REGRA PELA QUAL DESEJA MODIFICAR SEU VETOR ========{RESET}
[ 1 ] - MULTIPLICAR POR UM VALOR
[ 2 ] - ELEVAR A UM VALOR
[ 3 ] - REDUZIR A UMA FRAÇÃO
[ 4 ] - SUBSTITUIR NEGATIVOS POR NUMEROS ALEATÓRIOS DE UMA FAIXA
[ 5 ] - ORDENAR VALORES
[ 6 ] - EMBARALHAR VALORES
{BOLD}[ 0 ] - VOLTAR{RESET}
{MAGENTA}======================================================================={RESET}
""")


def menu():
    print(f"""{MAGENTA}============ MANIPULADOR DE VETORES ============={RESET}
[ 1 ] INICIALIZAR VETOR                                      
[ 2 ] MOSTRAR TODOS OS VALORES DO VETOR                   
[ 3 ] RESETAR VETOR                           
[ 4 ] VER QUANTIDADE DE ITENS NO VETOR      
[ 5 ] VER MENOR E MAIOR VALORES E SUAS POSIÇÕES
[ 6 ] SOMATÓRIO DOS VALORES                  
[ 7 ] MÉDIA DOS VALORES                      
[ 8 ] VALORES POSITIVOS E QUANTIDADE       
[ 9 ] VALORES NEGATIVOS E QUANTIDADE        
[ 10 ] ATUALIZAR TODOS OS VALORES POR UMA REGRA
[ 11 ] ADICIONAR NOVOS VALORES             
[ 12 ] REMOVER ITENS POR VALOR EXATO     
[ 13 ] REMOVER ITENS POR POSIÇÃO         
[ 14 ] EDITAR VALOR ESPECÍFICO POR POSIÇÃO   
[ 15 ] SALVAR VETOR EM UM ARQUIV0
[ 16 ] SAIR ( SALVAMENTO AUTOMÁTICO )

{BOLD}[ 17 ] INFORMAÇÕES ÚTEIS {RESET}
{MAGENTA}================================================={RESET}
""")


def main():
    utils.clean_screen()
    name = str(input(f"\n{LIGHT_GREEN}{BOLD}Digite Seu Nome de Usuário:{RESET} "))
    utils.clean_screen()

    utils.print_slow(f"\n{BLUE}Olá {LIGHT_YELLOW}{BOLD}{name}{RESET}{BLUE}, Bem Vindo ao Manipulador de Vetores{RESET}\n")
    utils.print_slow(f"{BLUE}Lembre-se de Que é Necessário {BOLD}Inicializar um Vetor{RESET} {BLUE}Para Ter Acesso às suas Funcionalidades{RESET}\n")

    opcao = 1
    while opcao != 16:
        menu()
        opcao = int(input(f"{CYAN}Digite a Funcionalidade:{RESET} "))

        if not 1 <= opcao <= 17:
            utils.clean_screen()

        if opcao == 1:
            utils.clean_screen()
            menu_leitura_arquivo()

            modo = int(input(f"\n{CYAN}Digite a Funcionalidade:{RESET} "))

            if modo == 1:
                tamanho,maximo,minimo = map(int,input(f"""\n{CYAN}Digite o Tamanho, Número Mínimo e Número Máximo do seu Vetor, Respectivamente{RESET} {BOLD}[Ex: 10 1 100]:{RESET}
--> """).split())
                vetor_atual = utils.get_random_vector(tamanho,maximo,minimo)

            if modo == 2:
                tamanho = int(input(f"\n{CYAN}Digite a Quantidade de Itens que o Vetor irá Conter:{RESET} "))
                vetor_atual = utils.create_vector(tamanho)

            if modo == 3:
                nome_arquivo = str(input(f"""\n{CYAN}Digite o Nome do Arquivo{RESET} {BOLD}[Ex: arquivo]:{RESET}
--> """)).strip() + ".txt"
                
                fin = open(nome_arquivo,"r")
                
                vetor_atual = utils.extract_file(fin)

            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")
            utils.wait_press_enter_and_clean()

        if opcao == 2:
            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

            utils.wait_press_enter_and_clean()

        if opcao == 3:
            valor_padrao = int(input(f"\n{CYAN}Qual Número Padrão Deseja Usar Para Resetar o Vetor?:{RESET} "))

            resultado = utils.reset_vector(vetor_atual,valor_padrao)
            vetor_atual = resultado

            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

            utils.wait_press_enter_and_clean()

        if opcao == 4:
            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}Quantidade de Valores -->{RESET} {len(vetor_atual)}\n")

            utils.wait_press_enter_and_clean()

        if opcao == 5:
            utils.clean_screen()
            menor,maior = utils.get_min_and_max(vetor_atual)
            posicao_menor,posicao_maior = utils.get_position_numbers(menor,maior,vetor_atual)


            print(f"""{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}

{LIGHT_GREEN}MENOR -->{RESET} {menor}
{LIGHT_GREEN}MAIOR -->{RESET} {maior}

{LIGHT_GREEN}POSIÇÃO MENOR{RESET} --> {posicao_menor}
{LIGHT_GREEN}POSIÇÃO MAIOR{RESET} --> {posicao_maior}\n""""")

            utils.wait_press_enter_and_clean()

        if opcao == 6:
            somatorio = utils.sum_values(vetor_atual)

            utils.clean_screen()

            print(f"\n{LIGHT_GREEN}Somatório dos Valores -->{RESET} {somatorio}\n")

            utils.wait_press_enter_and_clean()

        if opcao == 7:
            media = utils.get_media(vetor_atual)
            utils.clean_screen()

            print(f"\n{LIGHT_GREEN}Média dos Valores -->{RESET} {media:.2f}\n")

            utils.wait_press_enter_and_clean()

        if opcao == 8:
            parameter = 2
            numeros_positivos = utils.get_posivites_negatives(parameter,vetor_atual)

            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}NÚMEROS POSITIVOS NO VETOR -->{RESET} {numeros_positivos}")
            print(f"{LIGHT_GREEN}QUANTIDADE -->{RESET} {len(numeros_positivos)}\n")

            utils.wait_press_enter_and_clean()

        if opcao == 9:
            parameter = 1
            numeros_negativos = utils.get_posivites_negatives(parameter,vetor_atual)

            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}NÚMEROS NEGATIVOS NO VETOR -->{RESET} {numeros_negativos}")
            print(f"{LIGHT_GREEN}QUANTIDADE -->{RESET} {len(numeros_negativos)}\n")

            utils.wait_press_enter_and_clean()

        if opcao == 10:
            utils.clean_screen()

            opcao_regras = 1
            while opcao_regras != 0:
                menu_regras()
                opcao_regras = int(input(f"{CYAN}Digite a Funcionalidade:{RESET} "))

                if not 0 <= opcao <= 6:
                    utils.clean_screen()

                if opcao_regras == 1:
                    valor = float(input(f"\n{CYAN}Por Qual Valor Deseja Multiplicar o Vetor?:{RESET} "))

                    vetor_atual = utils.multiply_vector(vetor_atual,valor)

                    utils.clean_screen()
                    print(f"{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

                    utils.wait_press_enter_and_clean()

                if opcao_regras == 2:
                    valor = int(input(f"\n{CYAN}Por Qual Valor Deseja Elevar o Vetor?:{RESET} "))

                    vetor_atual = utils.elevate_vector(valor,vetor_atual)

                    utils.clean_screen()
                    print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

                    utils.wait_press_enter_and_clean()

                if opcao_regras == 3:
                    numerador,denominador = map(int,input(f"""\n{CYAN}Digite a Fração que Deseja Dividir{RESET} {BOLD}[Ex: 1/3]:{RESET}
--> """).split("/"))

                    vetor_atual = utils.division_vector(vetor_atual,numerador,denominador)

                    utils.clean_screen()
                    print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

                    utils.wait_press_enter_and_clean()

                if opcao_regras == 4:
                    min,max = map(int,input(f"""\n{CYAN}Digite o Valor Mínimo e Máximo do Novos Números, Respectivamente {RESET}{BOLD}[Ex: 1 10]:{RESET}
--> """).split())

                    vetor_atual = utils.replace_vector_negative(min,max,vetor_atual)

                    utils.clean_screen()
                    print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

                    utils.wait_press_enter_and_clean()

                if opcao_regras == 5:
                    vetor_atual = utils.sort_vector(vetor_atual)

                    utils.clean_screen()
                    print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

                    utils.wait_press_enter_and_clean()

                if opcao_regras == 6:
                    vetor_atual = utils.shuffle_vector(vetor_atual)

                    utils.clean_screen()
                    print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

                    utils.wait_press_enter_and_clean()

        if opcao == 11:
            utils.clean_screen()
            qtd_valores = int(input(f"\n{CYAN}Quantos Valores Deseja Adicionar?:{RESET} "))

            vetor_atual = utils.add_to_vector(qtd_valores,vetor_atual)

            print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

            utils.wait_press_enter_and_clean()

        if opcao == 12:
            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

            qtd_num_removidos = int(input((f"{CYAN}Quantos Valores Deseja Remover?:{RESET} ")))

            vetor_atual = utils.remover_exact_value(qtd_num_removidos,vetor_atual)

            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

            utils.wait_press_enter_and_clean()

        if opcao == 13:
            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

            qtd_num_removidos = int(input((f"{CYAN}Quantos Valores Deseja Remover?:{RESET} ")))

            vetor_atual = utils.remove_by_position(qtd_num_removidos,vetor_atual)

            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

            utils.wait_press_enter_and_clean()

        if opcao == 14:
            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

            posicao_editada = int(input(f"{CYAN}Qual Posição Deseja Editar?:{RESET} "))
            valor_novo = int(input(f"{CYAN}Que Valor Deseja Inserir na Posição?:{RESET} "))

            vetor_atual = utils.edit_value_by_position(vetor_atual,posicao_editada,valor_novo)

            utils.clean_screen()
            print(f"\n{LIGHT_GREEN}VETOR ATUAL -->{RESET} {vetor_atual}\n")

            utils.wait_press_enter_and_clean()

        if opcao == 15:
            utils.clean_screen()
            nome_arquivo = str(input((f"""\n{CYAN}Digite o Nome do Arquivo{RESET} {BOLD}[Ex: arquivo]:
--> {RESET}""")))

            utils.clean_screen()
            print("\n")
            utils.loading_simulator()
            utils.save_file(vetor_atual,nome_arquivo)
            utils.clean_screen()

            print(f'\n{YELLOW}{BOLD}ARQUIVO{RESET} {BOLD}"{nome_arquivo}" {YELLOW}SALVO COM SUCESSO{RESET}\n')

            utils.wait_press_enter_and_clean()

        if opcao == 16:
            nome_arquivo = utils.lowercase_name(name)

            utils.clean_screen()
            print("\n")
            utils.loading_simulator()
            utils.clean_screen()
            utils.save_file(vetor_atual,nome_arquivo)

            print(f'\n{YELLOW}{BOLD}ARQUIVO{RESET} {BOLD}"{nome_arquivo}" {YELLOW}SALVO AUTOMATICAMENTE{RESET}\n')

        if opcao == 17:
            utils.clean_screen()
            utils.print_slow(f"""\n{BLUE}Olá {LIGHT_YELLOW}{BOLD}{name}{RESET}{BLUE}, Nesta Página Você Encontrará Explicações e Curiosidades Sobre Alguns dos Códigos e Algoritmos Utilizados Nesta Aplicação. Sinta-se à Vontade para Explorar!{RESET}""")

            opcao_docs = 1
            while opcao_docs != 0:
                menu_documentacao()
                opcao_docs = int(input(f"\n{CYAN}Digite a Funcionalidade:{RESET} "))
                utils.clean_screen()

                if opcao_docs == 1:
                    utils.print_slow(docs.explicacao_bubble_sort,delay=0.005)
                    utils.wait_press_enter_and_clean(text="PRESSIONE ENTER PARA PROSSEGUIR")

                if opcao_docs == 2:
                    utils.print_slow(docs.explicacao_fisher_yates,delay=0.005)
                    utils.wait_press_enter_and_clean(text="PRESSIONE ENTER PARA PROSSEGUIR")

main()
