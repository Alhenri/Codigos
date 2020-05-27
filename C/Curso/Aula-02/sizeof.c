#include <stdio.h>

int main(void){
    char c; //O signed fica implicito na variavel, entao so temos 7 bits para valores positivos por o bit mais
    //significativo representa o sinal e divide o tamanho meio a meio
    printf("size of de char eh: %lu bytes", sizeof c); //lu = unsigned long, size of é um operador e retorna
    //o tamanho da variavel em bytes.
    return 0;
}