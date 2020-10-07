#include <stdio.h>
#include <stdbool.h>

void imprime(char *s){ //recebendo um array
    printf("Tamanho do array: %d\n", sizeof s);
    printf("endereco passado: %p\n", s);
    *s = 'b';
    s++;
    *s = 'c';
}

int retornaArray(){
    int a[] = {1, 2, 3, 4};
    return a;
}

int main(void) {

    /*

    // CASO EM ARRAY

    int a[] = { 2017, 2018, 2019};
    for (int i = 0; i < 3; i++)
    {
        //printf("%d\n", a[i]);
        //printf("%d\n", *a); // nesse caso ele ta printando o que está dentro dessa posição de memoria
        printf("%d\n", *a + i); // o mesmo que em cima só que avançando para o proximo endereço
        
    }
    printf("endereco de a: %p", a);
    */

    /* 
    // Com Inteiros

    int i = 2017;
    int *p;
    p = &i; // &i é o endereço de i

    printf("O endereco da variavel i eh: %p\n", &i); 
    printf("O endereco da variavel i eh: %p\n", p);
    printf("o valor de i eh: %d", *p); 
    */

    char u[] = { 0x66, 0x65, 0x72, 0x6e, 0x61, 0x6e, 0x64, 0x6f, 0x00 }; // criando o array

    printf("endereco antes da chamada: %p \n", &u); // endereco do array
    imprime(u); // passando o array como parametro

    puts(u);

    int *b = retornaArray();
    b++;
    printf("dado01: %p", *b);
    
    return 0;
}