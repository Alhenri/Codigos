#include <stdio.h>

int main(){
    int qtdN=0, vetor[100000], aux=0;
    while (scanf("%d ", &vetor[qtdN])!=-1)
    {
        qtdN++;
    }

    for (int k = 1; k < qtdN; k++) {
        for (int j = 0; j < qtdN - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                aux          = vetor[j];
                vetor[j]     = vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
    }
    
    for(int i=0; i<qtdN; i++){
        printf("%d ", vetor[i]);
    }

    int j=1, nImpar=0;
    for(int i=0; i<qtdN; i++){
        if(vetor[i]==vetor[i+1]){// se proximo for igual
            j++;
        }else
        {
            if(j%2==1){// se o j tiver achado n numeros impares
                nImpar=vetor[i];
                break;
            }else
            {
                j=1;
            }
        }
    }

    printf("\n%d", nImpar);
}