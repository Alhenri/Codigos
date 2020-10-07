#include <stdio.h>

int main(){
    int n, a; // n: sensores, a: amostras
    scanf("%d %d", &n, &a);

    int sensor[a][n];// cada amostra por sensor
    int valor[n][2]; // pega o maximo e o minimo de cada um
    int amostras[n];// amostras para ser normalizada
    int valorNorm[n]; // valores normalizados
    long prod=0;
    int posi=0, soma=0;

    for (int i = 0; i < n; i++)
    {
        valor[i][0]=10000; // valor minimo começa com valor maximo pra ser comparado
        valor[i][1]=0; // valor maximo começa com o minimo
    }
    

    for (int i=0; i < a; i++) // to pegando as amostras por sensores
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d ", &sensor[i][j]);
        }
    }

    for (int i = 0; i < n; i++)
    {
        scanf("%d ", &amostras[i]);
    }

    for (int i = 0; i < n; i++)// pegando menor e maior valor
    {
        for (int j = 0; j < a; j++)//vou rodar todas as amostras por sensor
        {
            if(sensor[j][i]<valor[i][0]){// se a amostra for menor que a que ja está
                valor[i][0] = sensor[j][i];
            }
            if(sensor[j][i]>valor[i][1]){
                valor[i][1] = sensor[j][i];
            }
        }
    }

    for (int i = 0; i < n; i++)//normalizando os valores
    {
        valorNorm[i] = (((amostras[i]-valor[i][0])*1000)/(valor[i][1]-valor[i][0]));
        if(valorNorm[i]<0){
            valorNorm[i]=0;
        }else
        if(valorNorm[i]>1000){
            valorNorm[i]=1000;
        }
        valorNorm[i] = 1000-valorNorm[i];
    }

    for (int i = 0; i < n; i++)
    {
        prod += i*1000*valorNorm[i];
        soma += valorNorm[i];
    }

    posi= prod/soma;
    
    // Hora de mostrar na tela

    for (int i = 0; i < n; i++)
    {
        printf("%d ", valor[i][1]);//valores maximos   
    }
    printf("\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", valor[i][0]);//valores minimos   
    }
    printf("\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", valorNorm[i]);//valores normalizados   
    }
    printf("\n%d", posi);
}