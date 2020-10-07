#include <stdio.h>
#include <string.h>


int main(){
    int flag0=1;

    while (flag0)
    {
        int n, m;
        scanf("%d %d", &n, &m);
        
        if (n==0&&m==0) //se for o fim da linha
        {
            flag0=0;
        }
        else 
        {
            char orig[n][21], trad[n][21];
            for (int i = 0; i < n; i++) // pegando a lista de palavras
            {
                scanf(" %s -> %s", orig[i], trad[i]);
            }

            for (int i = 0; i < m; i++)// pegando a frase e traduzindo
            {
                char frase[50], fraseTrad[50]={};
                
                scanf(" %[^\n]s", frase);
                for (int j = 0; j < strlen(frase); j++)
                {
                    for (int k = 0; k < n; k++) // pra cada letra da frase eu confiro de começa com a letra do erro
                    {
                        if (frase[j]==orig[k][0])
                        {
                            for (int l = 0; l < strlen(orig[k]); l++) // vou rodar pra cada letra do erro
                            {
                                if (frase[j+l]==orig[k][l]) // se forem iguais
                                {
                                    frase[j+l] = trad[k][l];
                                }
                            }
                            
                        }
                        
                    }
                    
                }
                
                
                printf("%s\n", frase);
            }            
        }
    }
}