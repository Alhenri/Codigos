#include <stdio.h>

int main(){
    int a=0, b=0, countPrimZeca=0; 
    scanf("%d %d", &a, &b);

    for (int i = a; i <= b; i++)
    {
        if(i>=5 && ehPrim(i)){ // maior que 5 e é primo
            int pa=2, pp=7;//como começa a partir do 5 -> 2 e o 7 como iniciais
            int c;
            int flag_pa = 1, flag_pp=1;

            for (c = i-1; c >= 0; c--)//procurar o primo anterior
            {   
                if(ehPrim(c)&&flag_pa){
                    pa=c;
                    flag_pa=0;
                }
            }
            c = i;

            do{ // pega o proximo primo
                c++;
                if(ehPrim(c)){
                    pp=c;
                    flag_pp=0;
                }
            }while (flag_pp);

            if (i == ((pa)+(pp))/2)
            {
                countPrimZeca++;
            }
            
        }
    }
    printf("%d", countPrimZeca);

    return 0;
}

int ehPrim(int n){
    if(n < 2){
        return 0;
    }
    for (int i = 2; i < n; i++)
    {
        if(n%i == 0){
            return 0;
        }
    }
    return 1;
}