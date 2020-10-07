#include <stdio.h>
#include <string.h>

int main(){
    int n, m, casos;
    scanf("%d %d", &n, &m);
    char matriz[n][m]; // linha e coluna
    
    // preenchendo a matriz
    for (int i = 0; i < n; i++)//talvez tenha erro aqui
    {
        scanf("\n"); //consumindo um \n
        for (int j = 0; j < m; j++)
        {
            scanf("%c ", &matriz[i][j]);
        }
    }

    scanf("%d", &casos);//pegando os casos
    
    // simulando os casos
    for (int i = 0; i < casos; i++)//cada caso agora
    {
        int x, y, dispo;
        char direc[21];
        memset(direc, '\0', 21);
        scanf("%d %d\n", &x, &y);
        scanf("%s", direc);
        scanf("%d", &dispo);

        if(strcmp(direc, "direita")==0){
            while (y < m) // vou mover nas colunas
            {
                if(matriz[x][y]=='#'){
                    dispo-=1;
                }else
                {
                    dispo-=2;
                }
                y++; //indo pra direita
            }
        }else
        if(strcmp(direc, "esquerda")==0){
            while (y >= 0) // vou mover nas colunas
            {
                if(matriz[x][y]=='#'){
                    dispo-=1;
                }else
                {
                    dispo-=2;
                }
                y--; //indo pra esquerda
            }
        }else
        if(strcmp(direc, "cima")==0){
            while (x >= 0) //vou mover nas linhas
            {
                if(matriz[x][y]=='#'){
                    dispo-=1;
                }else
                {
                    dispo-=2;
                }
                x--; // pq to indo pra cima
            }
        }
        else //baixo
        {
            while (x < n) //vou mover nas linhas
            {
                if(matriz[x][y]=='#'){
                    dispo-=1;
                }else
                {
                    dispo-=2;
                }
                x++; // pq to indo pra baixo
            }
        }

        if (dispo>0)
        {
            printf("O amor está no ar!\n");
        }else
        {
            printf("Vou voltar pra Limoeiro...\n");
        }
    }  
}