#include <stdio.h>

int main(){
    double saldo=0, opr[100][2], credito=0, debito=0;
    int count=0, flag=0, auxOp;
    
    while (flag==0)// pegando os valores do vetor
    {
        scanf("%d ", &auxOp);
        if(auxOp!=-1){
            opr[count][0]=auxOp;
            scanf("%lf", &opr[count][1]);
            count++;
        }else
        {
            flag=1;
        }
    }

    for (int i = 0; i <= count; i++)
    {
        if(opr[i][0]==1){ // se for credito
            saldo+=opr[i][1];
            credito+=opr[i][1];
        }
        else{
            saldo-=opr[i][1];
            debito+=opr[i][1];
        }
    }

    printf("Creditos: R$ %.2lf", credito);
    printf("Debitos: R$ %.2lf", debito);
    printf("Saldo: R$ %.2lf", saldo);
}