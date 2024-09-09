from random import randint

def recursiva_contar_vogais_consoantes(frase, char):
    if char <= 0:
        return 0
    
    



def recursiva_soma_vetor(a, b, quantidade):
    lista_vetores = []
    if quantidade <= 0:
        return 0, []
    
    valor = randint(a,b)
    soma, lista_valores = recursiva_soma_vetor(a, b, quantidade - 1)
    lista_valores.append(valor)

    return valor + soma, lista_valores


def recursiva_exponencial(numero, expoente):
    if expoente <= 0:
        return 1
    return numero * recursiva_exponencial(numero, expoente - 1)


def recursiva_multiplicacao(numero, multiplicador):
    if multiplicador <= 0:
        return 0
    return numero + recursiva_multiplicacao(numero, multiplicador - 1)

def recursiva_sequencia(n,b):
    if n >= b:
        return []
    
    return [n] + recursiva_sequencia(n + 1, b)


def recursiva_fibo(fat):
    if fat <= 1:
        return fat
    else:
        return recursiva_fibo(fat-1) + recursiva_fibo(fat-2)


def recursiva_fatorial(n):
    if n <= 1:
        return 1

    return n * recursiva_fatorial(n - 1)

def main():
    fatorial_sla = recursiva_fatorial(5)

    print(f"FATORIETIONS --> {fatorial_sla}")


    sequencia = 10
    print("FIBONATIONS --> ",end=" ")
    for valor in range(sequencia):
        print(recursiva_fibo(valor),end=" ")


    a = 1
    b = 10
    print("\nSEQUENCIETIONS DE NUMERATIONS --> ",end=" ")
    sequencia_numerica = recursiva_sequencia(a, b + 1)
    for valor in sequencia_numerica:
        print(valor, end=" ")


    numero = 5
    multiplicador = 5
    resultado_multi = recursiva_multiplicacao(numero,multiplicador)
    print(f"\from django.utils.translation import ungettextRESULTATIONS DA MULTIPLICATIONS --> {resultado_multi}")


    base = 5
    expoente = 3
    resultado_expo = recursiva_exponencial(base, expoente)
    print(f"RESULTATIONS DA EXPONETIONS --> {resultado_expo}")


    a = 1
    b = 20
    quantidade = 5
    (soma, valores) = recursiva_soma_vetor(a,b,quantidade)
    print(f"VETOR ALEATÓREITIONS --> {valores}")
    print(f"SOMATOREITIONS --> {soma}")

    
    frase = "literalmente_eu"
    char = len(frase)

main()
