import utils as utils

def menu():
    print("""        \033[35m====== MANIPULADOR DE VETORES =======\033[m
[ 1 ] - INICIALIZAR VETOR
[ 2 ] - MOSTRAR TODOS OS VALORES DO VETOR
[ 3 ] -
[ 4 ] - VER QUANTIDADE DE ITENS NO VETOR

          """)

def main():
    name = str(input(utils.color("Digite Seu Nome de Usuário: ",36)))
    utils.clean_screen()

    print(utils.color((f"\nOlá {name}, Bem Vindo ao Manipulador de Vetores, Verifique o Menu e Selecione sua Opção\n"),34))
    menu()

    choice = 1
    while choice != 0:
        choice = int(input(utils.color("\nDigite sua Escolha: ", 36)))

        if choice == 1:
            tamanho,maximo,minimo = map(int,input(utils.color("""\nDigite o Tamanho, Número Mínimo e Número Máximo do seu Vetor, Respectivamente [Ex: 10 1 100]:
--> """,36)).split())
            vetor_atual = utils.get_random_vector(tamanho,maximo,minimo)
            utils.clean_screen()
            print(utils.color("VETOR ATUAL -->",34),vetor_atual,"\n")
            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if choice == 2:
            print(utils.color("VETOR ATUAL -->",34),vetor_atual,"\n")
            utils.wait_press_enter()
            utils.clean_screen()
            menu()

        if choice == 3:
            pass

        if choice == 4:
            pass

        if choice == 5:
            pass

        if choice == 6:
            somatorio = utils.sum_values(vetor_atual)

            print(utils.color(f"\nO Somatório dos Vetores é {somatorio}",31))
            
main()
