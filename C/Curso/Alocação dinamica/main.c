#include <stdio.h>
#include <stdlib.h>
    
void *malloc_s(size_t size){ // fazendo uma função que nao retorna tipo especifico e recebe o numero de bytes
    void *ptr; // Ponteiro da memoria alocada
    ptr = malloc(size); // Criando uma alocação pra numero de bits

    if (ptr == NULL)
    {
        fprintf(stderr, "Memoria insuficiente");
        exit(1); // Fecha o programa mesmo fora da main
    }
    
    return ptr;
}

int main(){
    int *p; //ponteiro de um inteiro

    p = malloc_s(1*sizeof (int)); // Vai receber um ponteiro da alocação feita
    *p = 9; // Guarda o 9 no endereço que to apontando

    printf("No endereco %p esta guardado %d\n", p, *p);
    p = p+1;

    *p = 10;
    printf("No endereco %p esta guardado %d\n", p, *p);

    p = realloc(p, 6*sizeof(int)); // Pega o antigo ponteiro e retorna um novo com a nova alocação

    free(p); //libera a memoria alocada

}