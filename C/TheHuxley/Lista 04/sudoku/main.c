#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) //irá rodar para cada matriz
    {
        int matriz[9][9], flagL=0, flagC=0, flagM=0;
        // preenchendo a matriz
        for (int j = 0; j < 9; j++)
        {
            for (int k = 0; k < 9; k++)
            {
                scanf("%d ", &matriz[j][k]);
            }
        }
        //Verificando as linhas e colunas
        for (int j = 0; j < 9; j++)
        {   
            int vetorL[9];
            int vetorC[9];
            for (int k = 0; k < 9; k++)// preencho a linha e coluna
            {
                vetorL[k]=matriz[j][k];
                vetorC[k]=matriz[k][j];
            }
            bubble_sort(vetorL, 9); //ordeno o vetor linha
            bubble_sort(vetorC, 9); //ordeno o vetor coluna
            for (int k = 0; k < 9; k++)
            {
                if(vetorL[k]!=(k+1)){
                    flagL=1; //inidica erro na linha
                    //printf("Erro na linha %d\n", j);
                }
                if(vetorC[k]!=(k+1)){
                    flagC=1; //indica erro na coluna
                    //printf("Erro na coluna %d\n", j);
                }
            }
        }
        //Verificando as pequenas matrizes
        for (int j = 0; j < 3; j++) // São 3 matrizes por linha
        {
            for (int k = 0; k < 3; k++) // 3 matrizes por coluna
            {
                int vetorM[9], count=0;
                for (int l = 0; l < 3; l++) // E cada matriz pequena é 3x3
                {
                    for (int m = 0; m < 3; m++)
                    {
                        vetorM[count] = matriz[l+(3*j)][m+(3*k)];
                        count++;
                    }
                }
                bubble_sort(vetorM, 9);
                for (int l = 0; l < 9; l++)
                {
                    if(vetorM[l]!=(l+1)){ //possivelmente errado
                        flagM=1;
                    }
                }
            }
        }

        printf("Instancia %d\n", i+1);
        if((flagL==0)&&(flagC==0)&&(flagM==0)){
            printf("SIM\n\n");
        }else
        {
            printf("NAO\n\n");
        }
    }
}
void bubble_sort (int vetor[], int n) {
    int k, j, aux;

    for (k = 1; k < n; k++) {
        for (j = 0; j < n - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                aux          = vetor[j];
                vetor[j]     = vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
    }
}