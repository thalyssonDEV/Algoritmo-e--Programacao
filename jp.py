def my_len(list_t):
    count = 0

    for x in list_t:
        count += 1

    return count


#deus abençoe essa função 
#algoritmo de bolha pra ajudar na criação do sorted
def bubble(array_test):
    n = my_len(array_test)

    for i in range(n):
         
         for f in range(0, n-i-1):
            
            if array_test



def main():
    list_test = [2,6,4,8,1]
    
    new_list = my_sorted(list_test)

    print(new_list)


main()
