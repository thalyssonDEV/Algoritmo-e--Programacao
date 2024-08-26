import vetores_funcionalidades as utils
from cores import MAGENTA,RESET,CYAN


def menu_regras():
    print(f"""\n{MAGENTA}======= SELECIONE A REGRA PELA QUAL DESEJA MODIFICAR SEU VETOR ========{RESET}
[ 1 ] - MULTIPLICAR POR UM VALOR *
[ 2 ] - ELEVAR A UM VALOR *
[ 3 ] - REDUZIR A UMA FRAÇÃO *
[ 4 ] - SUBSTITUIR NEGATIVOS POR NUMEROS ALEATÓRIOS DE UMA FAIXA *
[ 5 ] - ORDENAR VALORES *
[ 6 ] - EMBARALHAR VALORES *
{MAGENTA}============================================================================{RESET}
""")


def menu():
    print(f"""{MAGENTA}============ MANIPULADOR DE VETORES ============={RESET}
[ 1 ] INICIALIZAR VETOR *                                       
[ 2 ] MOSTRAR TODOS OS VALORES DO VETOR *                      
[ 3 ] RESETAR VETOR *                           
[ 4 ] VER QUANTIDADE DE ITENS NO VETOR *        
[ 5 ] VER MENOR E MAIOR VALORES E SUAS POSIÇÕES ## ARRUMAR
[ 6 ] SOMATÓRIO DOS VALORES *                  
[ 7 ] MÉDIA DOS VALORES *                       
[ 8 ] VALORES POSITIVOS E QUANTIDADE *        
[ 9 ] VALORES NEGATIVOS E QUANTIDADE *         
[ 10 ] ATUALIZAR TODOS OS VALORES POR UMA REGRA*
[ 11 ] ADICIONAR NOVOS VALORES *              
[ 12 ] REMOVER ITENS POR VALOR EXATO *      
[ 13 ] REMOVER ITENS POR POSIÇÃO *           
[ 14 ] EDITAR VALOR ESPECÍFICO POR POSIÇÃO  *    
[ 15 ] SALVAR VETOR EM UM ARQUIV0 *  
[ 16 ] SAIR ( SALVAMENTO AUTOMÁTICO ) *

[ 99 ] --> INFORMAÇÕES ÚTEIS ;)
{MAGENTA}================================================={RESET}
""")

def main():
    utils.clean_screen()
    name = str(input(f"\n{CYAN}Digite Seu Nome de Usuário:{RESET} "))
    utils.clean_screen()

    utils.print_slow(utils.color((f"\nOlá {name}, Bem Vindo ao Manipulador de Vetores\n"),"azul_escuro"))
    utils.print_slow(utils.color("Lembre-se de Que é Necessário Inicializar um Vetor Para Ter Acesso às suas Funcionalidades\n","azul_escuro"))
    menu()

    opcao = 1
    while opcao != 16:
        opcao = int(input(utils.color("Digite a Funcionalidade: ","azul_claro")))

        if opcao == 1:
            tamanho,maximo,minimo = map(int,input(utils.color("""\nDigite o Tamanho, Número Mínimo e Número Máximo do seu Vetor, Respectivamente [Ex: 10 1 100]:
--> ""","azul_claro")).split())
            
            vetor_atual = utils.get_random_vector(tamanho,maximo,minimo)
            utils.clean_screen()
            
            print(utils.color("\nVETOR ATUAL -->","verde_claro"),vetor_atual,"\n")
            
            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 2:
            utils.clean_screen()
            print(utils.color("\nVETOR ATUAL -->","verde_claro"),vetor_atual,"\n")
            
            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 3:
            valor_padrao = int(input(utils.color("\nQual Número Padrão Deseja Usar Para Resetar o Vetor?: ","azul_claro")))

            resultado = utils.reset_vector(vetor_atual,valor_padrao)
            vetor_atual = resultado

            utils.clean_screen()
            print(utils.color("\nVETOR ATUAL -->","verde_claro"),resultado,"\n")

            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 4:
            utils.clean_screen()
            print(utils.color(f"\nQuantidade de Valores -->","verde_claro"),(len(vetor_atual)),"\n")
            
            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 5:
            utils.clean_screen()
            menor,maior = utils.get_min_and_max(vetor_atual)
            posicao_menor,posicao_maior = utils.get_position_numbers(maior,menor,vetor_atual)

            print(utils.color("MENOR -->","verde_claro"),menor)
            print(utils.color("MAIOR -->","verde_claro"),maior)
            print(utils.color("\nPOSIÇÃO MENOR -->","verde_claro"),posicao_menor)
            print(utils.color("POSIÇÃO MAIOR -->","verde_claro"),posicao_maior)

            utils.wait_press_enter()
            utils.clean_screen()
            menu()
        
        if opcao == 6:
            somatorio = utils.sum_values(vetor_atual)
            
            utils.clean_screen()
            
            print(utils.color(f"\nO Somatório dos Valores é {somatorio}\n","vermelho"))
            
            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 7:
            media = utils.get_media(vetor_atual)
            utils.clean_screen()

            print(utils.color(f"\nA Média dos Valores é {media:.2f}\n","vermelho"))

            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 8:
            parameter = 2
            numeros_positivos = utils.get_posivites_negatives(parameter,vetor_atual)

            print(utils.color("\nNÚMEROS POSITIVOS NO VETOR -->","verde_claro"),numeros_positivos)
            print(utils.color("QUANTIDADE -->","verde_claro"),len(numeros_positivos),"\n")

            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 9:
            parameter = 1
            numeros_negativos = utils.get_posivites_negatives(parameter,vetor_atual)

            print(utils.color("\nNÚMEROS NEGATIVOS NO VETOR -->","verde_claro"),numeros_negativos)
            print(utils.color("QUANTIDADE -->","verde_claro"),len(numeros_negativos),"\n")

            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 10:
            utils.clean_screen()
            menu_regras()

            opcao_regras = int(input(utils.color("Digite a Funcionalidade: ","azul_claro")))

            if opcao_regras == 1:
                valor = int(input(utils.color("\nPor Qual Valor Deseja Multiplicar o Vetor?: ","azul_claro")))

                resultado = utils.multiply_vector(vetor_atual,valor)
                vetor_atual = resultado

                utils.clean_screen()
                print(utils.color("VETOR ATUAL -->","verde_claro"),resultado,"\n")

                utils.wait_press_enter()
                utils.clean_screen()
                menu()

            if opcao_regras == 2:
                valor = int(input(utils.color("\nPor Qual Valor Deseja Elevar o Vetor?: ","azul_claro")))

                resultado = utils.elevate_vector(valor,vetor_atual)
                vetor_atual = resultado

                utils.clean_screen()
                print(utils.color("\nVETOR ATUAL -->","verde_claro"),resultado,"\n")

                utils.wait_press_enter()
                utils.clean_screen(
                    
                )
                menu()

            if opcao_regras == 3:
                numerador,denominador = map(int,input(utils.color("""\nDigite a Fração que Deseja Dividir [Ex: 1/3]:
--> ""","azul_claro")).split("/"))

                resultado = utils.division_vector(vetor_atual,numerador,denominador)
                vetor_atual = resultado

                utils.clean_screen()
                print(utils.color("\nVETOR ATUAL -->","verde_claro"),resultado,"\n")

                utils.wait_press_enter()
                utils.clean_screen()
                menu()
            
            if opcao_regras == 4:
                min,max = map(int,input(utils.color("""\nDigite o Valor Mínimo e Máximo do Novos Números, Respectivamente
[Ex: 1 10]:
--> ""","azul_claro")).split())

                resultado = utils.replace_vector_negative(min,max,vetor_atual)
                vetor_atual = resultado

                utils.clean_screen()
                print(utils.color("\nVETOR ATUAL -->","verde_claro"),resultado,"\n")

                utils.wait_press_enter()
                utils.clean_screen()
                menu()

            if opcao_regras == 5:
                resultado = utils.sort_vector(vetor_atual)
                vetor_atual = resultado

                utils.clean_screen()
                print(utils.color("\nVETOR ATUAL -->","verde_claro"),resultado,"\n")

                utils.wait_press_enter()
                utils.clean_screen()
                menu()

            if opcao_regras == 6:
                resultado = utils.shuffle_vector(vetor_atual)
                vetor_atual = resultado

                utils.clean_screen()
                print(utils.color("\nVETOR ATUAL -->","verde_claro"),resultado,"\n")

                utils.wait_press_enter()
                utils.clean_screen()
                menu()

        if opcao == 11:
            qtd_valores = int(input(utils.color("\nQuantos Valores Deseja Adicionar?: \n","azul_claro")))

            utils.clean_screen()
            resultado = utils.add_to_vector(qtd_valores,vetor_atual)
            vetor_atual = resultado
            
            print(utils.color("\nVETOR ATUAL -->","verde_claro"),resultado,"\n")
            
            utils.wait_press_enter()
            utils.clean_screen()
            menu() 

        if opcao == 12:
            utils.clean_screen()
            print(utils.color("\nVETOR ATUAL -->","verde_claro"),vetor_atual,"\n")

            qtd_num_removidos = int(input((utils.color("Quantos Valores Deseja Remover?: ","azul_claro"))))
            
            resultado = utils.remover_exact_value(qtd_num_removidos,vetor_atual)
            vetor_atual = resultado
                
            utils.clean_screen()
            print(utils.color("\nVETOR ATUAL -->","verde_claro"),resultado,"\n")

            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 13:
            utils.clean_screen()
            print(utils.color("\nVETOR ATUAL -->","verde_claro"),vetor_atual,"\n")
            
            qtd_num_removidos = int(input((utils.color("Quantos Valores Deseja Remover?: ","azul_claro"))))

            resultado = utils.remove_by_position(qtd_num_removidos,vetor_atual)
            vetor_atual = resultado

            utils.clean_screen()
            print(utils.color("\nVETOR ATUAL -->","verde_claro"),resultado,"\n")

            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 14:
            utils.clean_screen()
            print(utils.color("\nVETOR ATUAL -->","verde_claro"),vetor_atual,"\n")

            posicao_editada = int(input((utils.color("Qual Posição Deseja Editar?: ","azul_claro"))))
            valor_novo = int(input((utils.color("Que Valor Deseja Inserir na Posição?: ","azul_claro"))))

            vetor_atual = utils.edit_value_by_position(vetor_atual,posicao_editada,valor_novo)

            utils.clean_screen()
            print(utils.color("\nVETOR ATUAL -->","verde_claro"),vetor_atual,"\n")

            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 15:
            utils.clean_screen()
            nome_arquivo = str(input((utils.color("\nDigite o Nome do Arquivo: ","azul_claro"))))

            utils.save_file(vetor_atual,nome_arquivo)
            
            print(utils.color(f'\nARQUIVO "{nome_arquivo}" SALVO COM SUCESSO','laranja'),"\n")
            
            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if opcao == 16:
            nome_arquivo = utils.lowercase_name(name)

            utils.save_file(vetor_atual,nome_arquivo)


main()
