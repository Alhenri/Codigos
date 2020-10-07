#include <stdio.h>
#include <math.h>
#define fat(A)for(fat = 1; A > 1; A--)fat = fat * A;

int main(){
    int N, B, ID, D, IDescolhido; // N = maximo de pessoas conectadas
    float fat;
    float probEscolhida=1;
    float P;
    // B = banda requisitada por cada um
    scanf("%d %d", &N, &B);
    
    do
    {
        float pAux=0;
        scanf("%d %f %d", &ID, &P, &D); // D = capacidade maxima do roteado
        if(ID != -1){
            int usersExc = (D/B); // numero de usuários que excederam a capacidade
            for (int i = usersExc + 1; i <= N; i++) // alterei aqui
            {   
                int X = i; // alterei aqui
                int n_x = N - X;
                int Naux = N, Xaux = X, n_xaux = n_x;

                fat(Naux)
                float nfat = fat;

                fat(Xaux)
                float xfat = fat;

                fat(n_xaux)
                float n_xfat = fat;
                
                //printf("%d %d %f %d\n", X, N, P, n_x);
                //printf("%li %li %li\n", xfat, nfat, n_xfat);

                pAux += (nfat/(n_xfat*xfat)*(pow(P, X))*pow((1-P),n_x));

            }

            if(pAux < 0.0) pAux = 0.0; // alterei aqui
            
            if(pAux<probEscolhida){
                probEscolhida = pAux;
                IDescolhido = ID;
            }
            
        }
    } while (ID != -1);

    printf("O roteador escolhido foi o %d, com probabilidade de %.5f", IDescolhido, probEscolhida);
    
    return 0;
}