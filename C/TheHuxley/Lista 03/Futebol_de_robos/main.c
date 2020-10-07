#include <stdio.h>

int main(){
    char time[8], win;
    int part[4][2], Qwin[2][2], Swin[2];

    for (int i = 0; i < 8; i++)//times
    {
        scanf("%c\n", &time[i]);
    }

    for (int i = 0; i < 4; i++)//partidas
    {
        scanf("%d %d", &part[i][0], &part[i][1]);//guardo a ordem da partida e os indices dos times
    }
    scanf("\n");
    int count=0;
    for (int i = 0; i < 2; i++)//vencedor das quartas
    {
        for (int j = 0; j < 2; j++)
        {
            char aux;
            scanf("%c\n", &aux);
            
            if(aux=='A'){
                Qwin[i][j]=part[count][0];//o primero time
            }
            else
            {
                Qwin[i][j]=part[count][1];
            }
            count++;
        }
    }
    for (int i = 0; i < 2; i++)
    {
        char aux;
        scanf("%c\n", &aux);
        if(aux=='X'){
            Swin[i]=Qwin[i][0];
        }
        else
        {
            Swin[i]=Qwin[i][1];
        }
        
    }
    
    char aux;
    scanf("%c", &aux);
    if(aux == '#'){
        win=time[Swin[0]];
    }else
    {
        win=time[Swin[1]];
    }
    

    // Traduzindo os resultados
    
    for (int i = 0; i < 4; i++)
    {
        printf("Quartas de final %d: %c x %c\n", i+1, time[part[i][0]], time[part[i][1]]);
    }
    
    for (int i = 0; i < 2; i++)// so vai rodar 2 vezes por causa das duas incrementações
    {
        printf("Semifinal %d: %c x %c\n", i+1, time[Qwin[i][0]], time[Qwin[i][1]]);
    }
    
    printf("Final: %c x %c\n", time[Swin[0]], time[Swin[1]]);
    
    printf("O vencedor da competição de futebol de robôs foi %c!", win);
}