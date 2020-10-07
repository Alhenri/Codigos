#include <stdio.h>

int main(){
    int t=0;
    scanf("%d",&t); //quantidade de vetores 

    for (int i = 0; i < t; i++) // dentro de um vetor
    {   
        // pegando informação
        int n=0, nSeq=1;
        scanf("%d", &n); // tamanho dos vetores
        int vetor[n], vetorSeq[n], nSeqDef=1, vetorSeqDef[n];

        for (int j = 0; j < n; j++) //preenchendo o vetor total
        {
            scanf("%d", &vetor[j]);
        }  

        // processando
        for (int j = 0; j < n; j++) // preencho o vetor com a sequencia
        {
            if((vetor[j]>vetor[j+1])&&j<n-1){// se proximo numero da sequencia for menor
                
                //printf("%d - %d\n", vetor[j], vetor[j+1]);
                if(nSeq==1){ // se iniciar uma nova sequencia
                    vetorSeq[0]=vetor[j];
                }
                vetorSeq[nSeq]=vetor[j+1];
                nSeq++;
            }
            else //cheguei no fim dessa sequencia
            {   
                if(nSeq>nSeqDef){ // se a nova sequencia for maior
                    for (int k = 0; k < nSeq; k++)// atualiza o vetor definitivo
                    {
                        vetorSeqDef[k]=vetorSeq[k];
                    }
                    nSeqDef=nSeq;
                    nSeq=1;
                }
                else // se não for maior
                {
                    nSeq=1; // reseto a variável e vou procurar o proximo
                }  
            }
            
        }
        //Hora de mostrar na tela
        printf("Nseq: %d", nSeqDef);
        if(nSeqDef>1){
            printf("%d\n", nSeqDef);
            for (int j = 0; j < nSeqDef; j++)
            {
                printf("%d ", vetorSeqDef[j]);
            }
        }
        else
        {
            printf("0");
        }
        printf("\n");
    }
}