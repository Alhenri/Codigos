#include <stdio.h>
#include <stdlib.h>
#include <limits.h>// Valores de limites de vtipos de variaveis
#include <stdint.h>// para se usar o uint8_t ou outros valores

int main(){
    // unsigned int i = UINT_MAX;
    //unsigned long long i = 18446744073709551614;
    // long long i = UINT_MAX;
    register int i = 0;//coloca num registrador

    i++; //ela irá para o valor minimo

    printf("O valor de i (int): %li bytes / %li bits \n", sizeof i, sizeof i*8);

    printf("valor de i: %d\n", i); // Para usigned int usasse o '%u'

    return 0;
}
