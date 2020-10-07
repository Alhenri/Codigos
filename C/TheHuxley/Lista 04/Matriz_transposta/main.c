#include <stdio.h>

int main(){
    int x, y;
    scanf("%d %d", &x, &y);
    int matriz[x][y];

    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            scanf("%d ", &matriz[i][j]);
        }
        scanf("\n"); //consumir um enter
    }

    for (int i = 0; i < y; i++)
    {
        for (int j = 0; j < x; j++)
        {
            printf("%d ", matriz[j][i]);
        }
        printf("\n");
    }
}