def clean_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def remove_space(word):
    new_word = ''
    for character in word:

        if character != ' ':
            new_word += character
        else:
            continue

    return new_word

def option_1(fin,quantity_letters):
    for line in fin:

        word = line.strip()
        formated_word = remove_space(word)
        if len(formated_word) > quantity_letters:
            print(formated_word)
        else:
            continue

def option_2(fin,letter_to_remove):          
    for line in fin:

        word = line.strip()
        formated_word = remove_space(word)

        new_word = ''
        for character in formated_word:

            if character != letter_to_remove:
                new_word += character
        
        if new_word != '':
            print(new_word)

def option_3(fin,removed_words):
    list_removed_words = []
    for index in removed_words:
        
        if index != " ":
            list_removed_words.append(index)

    words_without_prohibited_letters = 0
    for line in fin:
        for letter in line:
            if letter in list_removed_words:
                break
            else:
                words_without_prohibited_letters += 1
    
    print(f"O Arquivo Possui {words_without_prohibited_letters} Palavras que Não Incluem esses Caracteres")

def option_4(word):
    list_letters = []
    for index in removed_words:

        if index != " ":
            list_letters.append(index)


def show_menu():
    print("""\033[36m
        ======== WORD-PLAY ========\033[m
\033[33m[ 1 ] - PALAVRAS COM MAIS DE 20 LETRAS
[ 2 ] - PALAVRAS SEM A LETRA "E"
[ 3 ] - PALAVRAS SEM "X" LETRAS
[ 0 ] - SAIR
\033[m""")

def main():
    show_menu()
    
    fin = open(str(input("""Informe o Arquivo [Ex: \033[31marquivo.txt\033[m]:
--> """)), "r")
    clean_screen()
    print(f"ARQUIVO \033[33m{fin.name}\033[m CARREGADO COM SUCESSO")
    input("\033[34m\nPressione ENTER para continuar\033[m")
    clean_screen()
    
    choice = 1
    while choice != 0:
        show_menu()
        choice = int(input("Escolha a Opção: "))
        clean_screen()

        if choice == 1:
            option_1(fin,20)

        if choice == 2:
            option_2(fin,"e")

        if choice == 3:
            removed_words = str(input("""Digite as Letras que Deseja Remover Separadas por Espaço [\033[31mEx: a b c d\033[m]:
--> """))
            option_3(fin,removed_words)
        
        if choice == 4:
            word = str(input("Digite a Palavra: "))

            option_4()

        fin = open(fin.name)

main()
