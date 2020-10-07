#include <stdio.h>

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if(a<0 || b<0 || c<0)
    {
        printf("esses dados nao valem");
    }else
    {   
        int ps = b-a; // gols do primeiro pro segundo ano
        int st = c-b; // gols do segundo pro terceiro

        if((ps>0 && st<=0)||(ps>0 && st<=ps)||(ps<0 && st<0 && st<=ps)||(ps==0 && st<0))
        {
            printf(":(");
        }else{
            printf(":)");
        }
    }
}