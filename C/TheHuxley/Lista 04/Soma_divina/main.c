#include <stdio.h>

int main(){
    int ord;
    scanf("%d", &ord);
    int m1[ord][ord], m2[ord][ord], mr[ord][ord];

    for (int i = 0; i < ord; i++)
    {
        for (int j = 0; j < ord; j++)
        {
            scanf("%d", &m1[i][j]);
        }
    }

    for (int i = 0; i < ord; i++)
    {
        for (int j = 0; j < ord; j++)
        {
            scanf("%d", &m2[i][j]);
        }
    }

    if(ord==0){
        printf("Vazia");
    }else
    {
        for (int i = 0; i < ord; i++)
        {
            for (int j = 0; j < ord; j++)
            {
                printf("%d\n", (m1[i][j]+m2[i][j]));
            }
        }
    }
}