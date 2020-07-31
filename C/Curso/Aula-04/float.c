#include <stdio.h>
#include <stdlib.h>
#include <limits.h>// Valores de limites de vtipos de variaveis
#include <stdint.h>// para se usar o uint8_t ou outros valores

int main(){
    float f = 1; // 3*100

    printf("O tamanho de f (float): %li bytes / %li bits \n", sizeof f, sizeof f*8);

    printf("valor de f: %f\n", 10/3); //em dizima periodica o resultado sai 0

    return 0;
}
