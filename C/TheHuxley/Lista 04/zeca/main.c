#include <stdio.h>

int main(){
    int m1[3][3]={}, m2[3][3]={}, m1xm2[3][3]={};

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            scanf("%d ", &m1[i][j]);
        }
        scanf("\n");
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            scanf("%d ", &m2[i][j]);
        }
        scanf("\n");
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++) // vai construir o primeiro numero da matriz
        {       
            for (int l = 0; l < 3; l++)
            {
                m1xm2[i][j] += m1[i][l]*m2[l][j]; 
                //printf("%d x %d + ", m1[i][l], m2[l][j]);
            }
            //printf("\n");
        }
    }

    for (int i = 0; i < 3; i++)
    {
        printf("%d %d %d\n", m1xm2[i][0],m1xm2[i][1],m1xm2[i][2]);
    }
    
}