#include <stdio.h>

int main(){
    int N=0;
    scanf("%d", &N);
    int vetorO[N], vetor[N], same=0, pos[N], valor[N];
    
    for(int i=0; i<N; i++){
        scanf("%d", &vetorO[i]);
        vetor[i]=vetorO[i];//fazendo uma copia do vetor para ordenar
    }

    int aux;

    for (int k = 1; k < N; k++) {

        for (int j = 0; j < N - 1; j++) {

            if (vetor[j] > vetor[j + 1]) {
                aux          = vetor[j];
                vetor[j]     = vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
    }

    for(int i=0; i<N; i++){
        if(vetorO[i]==vetor[i]){
            valor[same]=vetorO[i];
            pos[same]=i;
            same++;
        }
    }

    printf("%d\n", same); // mostro a quantidade

    for(int i=0; i<same; i++){
        printf("%d %d\n", valor[i], pos[i]);
    }

}