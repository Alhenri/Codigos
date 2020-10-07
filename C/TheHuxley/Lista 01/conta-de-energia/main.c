#include <stdio.h>

int main(){
    int kwh;
    scanf("%d", &kwh);

    if(kwh>=100 && kwh<300)
    {
        printf("%.2f\n%.2f", kwh*1.55, 1.55);
    }else
    if(kwh>=300 && kwh<575)
    {
        printf("%.2f\n%.2f", kwh*1.75*1.1, 1.75);
    }else
    if(kwh>=575)
    {
        printf("%.2f\n%.2f", kwh*2.15*1.1, 2.15);
    }else // até 99
    {
        float valor = kwh*1.35;
        if (valor<35)
        {
            printf("%.2f\n%.2f", 35.00, 1.35);
        }else
        {
            printf("%.2f\n%.2f", valor, 1.35);
        }
        
    }
}