def clean_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def remove_space(word):
   
    new_word = ''
    for character in word:
        if character != ' ':
            new_word += character
    return new_word

def option_1(fin, quantity_letters):
    
    results = []
    for line in fin:
        word = line.strip()
        formatted_word = remove_space(word)
        
        if len(formatted_word) > quantity_letters:
            results.append(formatted_word)
    return results

def option_2(fin, letter_to_remove):
    
    results = []
    total_words = 0
    count_without_letter = 0

    for line in fin:
        words = line.strip().split()
        total_words += len(words)

        for word in words:
            formatted_word = remove_space(word)
            
            if letter_to_remove not in formatted_word:
                results.append(formatted_word)
                count_without_letter += 1

    if total_words > 0:
        percentage = (count_without_letter / total_words) * 100
    else:
        percentage = 0

    return results, percentage

def option_3(fin, removed_words):
    
    list_removed_words = [index for index in removed_words if index != " "]
    words_without_prohibited_letters = 0
    for line in fin:
        words = line.strip().split()
        
        for word in words:
            
            if all(letter not in list_removed_words for letter in word):
                words_without_prohibited_letters += 1
    return words_without_prohibited_letters

def option_4(fin, characters_in_word):
    
    list_letters = [index for index in characters_in_word if index != " "]

    count_words_with_letters = 0
    for line in fin:
        words = line.strip().split()

        for word in words:
            formatted_word = remove_space(word)
            contains_letter = False

            for letter in list_letters:
                
                if letter in formatted_word:
                    contains_letter = True
                    break
            if contains_letter:
                count_words_with_letters += 1

    return count_words_with_letters

def option_5(fin, required_letters):
    list_required_letters = [index for index in required_letters if index != " "]

    count_words_with_all_letters = 0
    for line in fin:
        words = line.strip().split()

        for word in words:
            formatted_word = remove_space(word)
            has_all_letters = True

            for letter in list_required_letters:
                
                if letter not in formatted_word:
                    has_all_letters = False
                    break
            if has_all_letters:
                count_words_with_all_letters += 1

    return count_words_with_all_letters

def option_6(fin):
    results = []
    count_words_alphabetical = 0

    for line in fin:
        words = line.strip().split()

        for word in words:
            formatted_word = remove_space(word)
            is_alphabetical = True

            for i in range(len(formatted_word) - 1):
                if formatted_word[i] > formatted_word[i + 1]:
                    is_alphabetical = False
                    break

            if is_alphabetical:
                results.append(formatted_word)
                count_words_alphabetical += 1

    return results, count_words_alphabetical

def show_menu():
    print("""\033[36m
      ======== WORD-PLAY ========\033[m
\033[33m[ 1 ] - PALAVRAS COM MAIS DE 20 LETRAS
[ 2 ] - PALAVRAS SEM A LETRA "E"
[ 3 ] - PALAVRAS SEM "X" LETRAS
[ 4 ] - PALAVRAS COM LETRAS ESPECÍFICAS
[ 5 ] - PALAVRAS COM LETRAS OBRIGATÓRIAS
[ 6 ] - PALAVRAS COM LETRAS EM ORDEM ALFABÉTICA
[ 0 ] - SAIR
\033[m""")

def main():
    show_menu()

    filename = input("""Informe o Arquivo [Ex: \033[31marquivo.txt\033[m]:
--> """)
    clean_screen()
    print(f"ARQUIVO \033[33m{filename}\033[m CARREGADO COM SUCESSO")
    input("\033[34m\nPressione ENTER para continuar\033[m")
    clean_screen()

    choice = 1
    while choice != 0:
        show_menu()
        choice = int(input("Escolha a Opção: "))
        clean_screen()

        if choice == 1:
            fin = open(filename, "r")
            results = option_1(fin, 20)
            for result in results:
                print(result)
            fin.close()

        elif choice == 2:
            fin = open(filename, "r")
            results, percentage = option_2(fin, "e")
            for result in results:
                print(result)
            print(f'\n\033[35mA Porcentagem de Palavras Que Não Contêm a Letra "E" é {percentage:.2f}%\033[m')
            fin.close()

        elif choice == 3:
            removed_words = input("""Digite as Letras que Deseja Remover Separadas por Espaço [\033[31mEx: a b c d\033[m]:
--> """)
            fin = open(filename, "r")
            words_without_prohibited_letters = option_3(fin, removed_words)
            print(f"\033[35mO Arquivo Possui {words_without_prohibited_letters} Palavras que Não Incluem esses Caracteres\033[m")
            fin.close()

        elif choice == 4:
            fin = open(filename, "r")
            characters_in_word = input("""Digite as Letras que Devem Estar Contidas nas Palavras [\033[31mEx: a b c d\033[m]:
--> """)
            count_words_with_letters = option_4(fin, characters_in_word)
            print(f"\033[95mO Arquivo Possui {count_words_with_letters} Palavras que Contêm Pelo Menos 1 Caractere da Lista\033[m")
            fin.close()

        elif choice == 5:
            fin = open(filename, "r")
            required_letters = input("""Digite as Letras que Devem Estar Presentes em Todas as Palavras [\033[31mEx: a b c d\033[m]:
--> """)
            count_words_with_all_letters = option_5(fin, required_letters)
            print(f"\033[92mO Arquivo Possui {count_words_with_all_letters} Palavras que Contêm Todas as Letras Obrigatórias\033[m")
            fin.close()

        elif choice == 6:
            fin = open(filename, "r")
            results, count_words_alphabetical = option_6(fin)
            for result in results:
                print(result)
            print(f"\n\033[96mO Arquivo Possui {count_words_alphabetical} Palavras cujas Letras Estão em Ordem Alfabética\033[m")
            fin.close()

main()
