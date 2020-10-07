#include <stdio.h>

int main(){
    int n, x0, x1, y0, y1, z0, z1;
    int palheta=0, corda=0, pedal=0; 
    scanf("%d", &n);
    scanf("%d %d %d %d %d %d", &x0, &x1, &y0, &y1, &z0, &z1);
    int flag=0;

    for (int i = x0; i < x1; i++)
    {
        for (int j = y0; j < y1; j++)
        {
            for (int k = z0; k < z1; k++)
            {
                int somaMaior = palheta+corda+pedal;
                int somaAtual = i+j+k;
                if((somaAtual > somaMaior) && (somaAtual <= n)){ //se ele for mais custo x beneficio
                    palheta = i;
                    corda = j;
                    pedal = k;
                }else
                if(somaAtual == somaMaior){ //mesmo custo x beneficio
                    if(i < palheta){ // se a palheta for mais barata
                        palheta = i;
                        corda = j;
                        pedal = k;
                    }else
                    if((i == palheta)&& (k < pedal)){ // se o pedal for mais barato
                        palheta = i;
                        corda = j;
                        pedal = k;
                    }
                }
            }
            
        }
        
    }
    if((palheta>0)&&(corda>0)&&(pedal>0))
    {
        printf("S\n");
        printf("%d %d %d", palheta, corda, pedal);
    }else
    {
        printf("N\n");
    }
    
    return 0;
}