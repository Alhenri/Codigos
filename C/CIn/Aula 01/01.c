#include <stdio.h> //lib que genrencia os comandos de entrada e saida do teclado

#define PI 3.14
#define perim(r) (2*PI*r) // troca um expressão pela outra (macro)


int main(int argc, char *argv[]){
    printf("%s\n", argv[0]);
    printf("Perimetro=%4.2f\n", perim(5)); // 4.2: 4 numeros ao todo e 2 casas decimais
    char p[] = "teste";
    printf("%10s", p);
    return 0;
}