#include <stdio.h>

int main(void){
    int ret = 0;

    //ret = printf("Teste de retorno \n");
    printf("Teste de retorno \n");
    //printf("retorno do printf() anterior: %d", ret);
    printf("%d - %d - %d - %d", ret, 10, 0xa, 'A'); //0xa é 10 em hexadecimal a função recebendo como espaço um %d
    //será tudo convertido em inteiro (%x = hexa, %c = caracter).
    //\n = %c -> 10

    return 0;

}