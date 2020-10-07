#include <stdio.h>
#include <string.h>

typedef struct {
    int id;
    char desc[50];
    float valor;
} Produto;


int main(){
    int n, flag=1;
    float preco=0;
    scanf("%d", &n);
    Produto produto[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &produto[i].id);
        scanf(" %[^\n]s", produto[i].desc);
        scanf("%f", &produto[i].valor);
    }

    while (flag)
    {
        int qtde, idaux, flag2=1, pos;
        scanf("%d", &idaux);

        // Verificando a validade do pedido
        for (int j = 0; j < n; j++)
        {
            if (idaux==produto[j].id)// Então existe
            {
                pos=j; //recebo a posição do produto
                flag2=0;
            }
        }
        
        if (idaux!=0)
        {
            scanf("%d", &qtde);

            if (qtde>=0&&!flag2)
            {
                preco+= qtde*produto[pos].valor;
            }
        }
        else
        {
            flag=0;
        }
    }

    printf("%.2f", preco);
}