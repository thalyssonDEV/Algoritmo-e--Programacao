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
    total_words = 0
    deleted_words = 0
    for line in fin:
        total_words += 1

        word = line.strip()
        formated_word = remove_space(word)

        new_word = ''
        for character in formated_word:

            if character != letter_to_remove:
                new_word += character
        deleted_words += 1
        
        if new_word != '':
            print(new_word)
    
    print(total_words)
    print(deleted_words)

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
    
    print(f"\033[35mO Arquivo Possui {words_without_prohibited_letters} Palavras que Não Incluem esses Caracteres\033[m")

def option_4(word,characters_in_word):
    list_letters = []
    for index in characters_in_word:

        if index != " ":
            list_letters.append(index)

    for letter in word:
        if letter in list_letters:
            print("\033[95mA Palavra Contém Pelo Menos 1 Caractere da Lista\033[m")
            break
    else:
        print("\033[95mA Palavra Não Contém Nenhum Caractere da Lista\033[m")
    
# def option_5(fin,mandatory_letters):
#     list_letters = []
#     for index in mandatory_letters:
        
#         if index != " ":
#             list_letters.append(index)

#     for lines in fin:
#         for letters in lines:
#             if letters not in list_letters:
#                 break
#         print(lines)

def show_menu():
    print("""\033[36m
        ======== WORD-PLAY ========\033[m
\033[33m[ 1 ] - PALAVRAS COM MAIS DE 20 LETRAS
[ 2 ] - PALAVRAS SEM A LETRA "E"
[ 3 ] - PALAVRAS SEM "X" LETRAS
[ 4 ] - EM MANUTENÇÃO
[ 5 ] - 
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
            characters_in_word = str(input("""Digite as Letras que Devem estar Contidas na Palavra [\033[31mEx: a b c d\033[m]:
--> """))

            option_4(word,characters_in_word)

        fin = open(fin.name)

#         if choice == 5:
#             mandatory_letters = str(input("""Digite as Letras Obrigatórias nas Palavras [\033[31mEx: a b c d\033[m]:
# --> """))
#             option_5(fin,mandatory_letters)

main()
