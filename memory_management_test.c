#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void) {
    int quantidade, valor;
    bool is_last = false;
    
    printf("Digite a Quantidade de Elementos no Vetor: ");
    scanf("%d", &quantidade);
    
    char *vector = (char *)malloc(quantidade * sizeof(char));
    
    if (vector == NULL) {
        printf("ERRO NA ALOCAÇÃO DE MEMÓRIA\n");
        return 1;
    }
    
    printf("Digite os Elementos Separados Por Espaço: ");
    for (int i = 0; i < quantidade; i++) {
        scanf(" %c", &valor);
        vector[i] = valor;
    }
    
    printf("\nSEU VETOR --> ");
    printf("[");
    for (int i = 0; i < quantidade; i++) {
        if (i == quantidade - 1) {
            is_last = true;
        }
        if (!is_last){
            printf("%c, ", vector[i]);
        } else{
          printf("%c]", vector[i]);  
        }
    }
    
    free(vector);
    return 0;
}
