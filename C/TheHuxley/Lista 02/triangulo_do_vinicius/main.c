#include <stdio.h>

int main(){
    char c;
    int lin=0, col=0;
    scanf("%c", &c);
    lin = (int)c - 64; // Do 'A' ate o &c
    col = (2*lin)-1;

    for (int i = 0; i < lin; i++) // escreve as linhas
    {
        
        int letras = 2*i +1; // quantidade de letras nessa linha
        int pontosl = (col - letras)/2; // quantidade de pontos laterais
        int letrasl = ((letras-1)/2);
        char aux;
        
        for (int g = 0; g < pontosl; g++) //escreve os pontos a esquerda
        {
            printf(".");
        }
        for (int g = 0; g <= letrasl; g++) // escreve as letras a direita
        {   
            aux= 65+g;
            printf("%c", aux);
        }

        for (int g = aux-1; g >= 'A'; g--) // escreve as letras a direita
        {
            printf("%c", g);
        }
        
        for (int g = 0; g < pontosl; g++) //escreve os pontos a esquerda
        {
            printf(".");
        }
        printf("\n");
    }
    
}