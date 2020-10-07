#include <stdio.h>
#define maior(a,b)(a>b?a:b)
#define menor(a,b)(a<b?a:b)

int main(){
    char p[3], q[3];
    int soma=0;
    scanf("%c %c %c", &q[0], &q[1], &q[2]);

    p[2] = (char)maior(q[0], maior(q[1], q[2]));
    p[0] = (char)menor(q[0], menor(q[1], q[2]));
    soma = q[0]+q[2]+q[1];
    p[1] = (char)soma-(p[0]+p[2]);

    if((p[0]>'Z' || p[0]<'A')||(p[1]>'Z' || p[1]<'A')||(p[2]>'Z' || p[2]<'A'))
    {
        printf("Etiquetas erradas!");
    }else
    {
        int hasVog=0; // flag que diz se tem vogal ou n
        for (int i = 0; i < 3; i++)
        {
            if (p[i]=='A'||p[i]=='E'||p[i]=='I'||p[i]=='O'||p[i]=='U')
            {
                hasVog=1;
            }
        }
        
        if((p[1]==p[0]+1) && (p[2]==p[1]+1)){
            hasVog?printf("Sequência quase perfeita."):printf("Sequência perfeita.");
        }else
        if((p[1]==p[0]+2) && (p[2]==p[1]+2)){
            hasVog?printf("Bissequência quase perfeita."):printf("Bissequência perfeita.");
        }else
        if((p[1]==p[0]+3) && (p[2]==p[1]+3)){
            hasVog?printf("Trissequência quase perfeita."):printf("Trissequência perfeita.");
        }
        else{
            printf("Só umas letras ai...");
        }
        
    }

    return 0;
}