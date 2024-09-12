#include <stdio.h>
#include <stdlib.h>

void showMenu() {
    printf("\n\n[ 1 ] ADICIONAR VALORES\n");
    printf("[ 2 ] REMOVER VALORES\n");
    printf("[ 0 ] SAIR\n");
}

void clearScreen() {
#if defined(_WIN32) || defined(_WIN64)
    system("cls");
#else
    system("clear");
#endif
}

int *addNumbers(int *vector, int *qtd, int qtdNumerosToAdd) {
    vector = (int *)realloc(vector, (*qtd + qtdNumerosToAdd) * sizeof(int));

    if (vector == NULL) {
        printf("ERRO NA REALOCAÇÃO DE MEMÓRIA\n");
        exit(1);
    }
    *qtd += qtdNumerosToAdd;

    return vector;
}

void removeNumber(int *vector, int *qtd, int valueToRemove) {
    int i, j;
    int found = 0;

    for (i = 0; i < *qtd; ) {
        if (vector[i] == valueToRemove) {
            found = 1;
            // Move todos os elementos após o valor removido para a esquerda
            for (j = i; j < *qtd - 1; j++) {
                vector[j] = vector[j + 1];
            }
            // Reduz o tamanho do vetor
            (*qtd)--;
            // Não incrementa 'i', pois o valor na posição 'i' foi substituído
        } else {
            i++;
        }
    }

    if (!found) {
        printf("\nVALOR NÃO ENCONTRADO NO VETOR\n");
    }
}

void showVector(int *vector, int qtd) {
    printf("\nSEU VETOR --> ");
    printf("[");
    for (int i = 0; i < qtd; i++) {
        if (i == qtd - 1) {
            printf("%d]", vector[i]);
        } else {
            printf("%d, ", vector[i]);
        }
    }
    printf("\n");
}

int *addVector(int qtd) {
    int *vector = (int *)malloc(qtd * sizeof(int));

    if (vector == NULL) {
        printf("ERRO NA ALOCAÇÃO DE MEMÓRIA\n");
        exit(1);
    }
    return vector;
}

int main(void) {
    int qtd, choice;

    printf("Digite a Quantidade de Elementos no Vetor: ");
    scanf("%d", &qtd);

    int *vector = addVector(qtd);

    printf("Digite os Elementos Separados Por Espaço ou Linha: ");
    for (int i = 0; i < qtd; i++) {
        scanf("%d", &vector[i]);
    }

    choice = 1;
    while (choice != 0) {
        clearScreen();
        showVector(vector, qtd);
        showMenu();

        printf("\nDigite sua Funcionalidade: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: {
                int qtdNumerosToAdd;

                printf("\nDigite Quantos Elementos Deseja Adicionar: ");
                scanf("%d", &qtdNumerosToAdd);

                vector = addNumbers(vector, &qtd, qtdNumerosToAdd);

                printf("\nDigite os Números a Adicionar Separados Por Espaço ou Linha: ");
                for (int i = qtd - qtdNumerosToAdd; i < qtd; i++) {
                    scanf("%d", &vector[i]);
                }
                break;
            }

            case 2: {
                int qtdNumerosToRemove, valueToRemove;

                printf("\nDigite Quantos Elementos Deseja Remover: ");
                scanf("%d", &qtdNumerosToRemove);

                printf("\nDigite os Números a Remover Separados Por Espaço ou Linha: ");
                for (int i = 0; i < qtdNumerosToRemove; i++) {
                    scanf("%d", &valueToRemove);
                    removeNumber(vector, &qtd, valueToRemove);
                }
                break;
            }

            case 0:
                printf("Saindo...\n");
                break;

            default:
                printf("Opção Inválida! Tente novamente.\n");
                break;
        }
    }
    free(vector);

    return 0;
}
