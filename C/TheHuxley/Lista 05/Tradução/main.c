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
                int c=0, posAnt=0;
                
                while (frase[c]!='\0') // lendo a frase ate o final
                {
                    char palavra[30]={};
                    if (frase[c]==' '||frase[c+1]=='\0')
                    {
                        if(posAnt==0){ //Na primeira palavra
                            strncpy(palavra,(frase+posAnt), (c-posAnt));
                        }else //Na ultima palavra
                        if(frase[c+1]=='\0'){
                            strncpy(palavra,(frase+posAnt+1), (c-posAnt));
                        }else // Nas palavras do meio
                        {
                            strncpy(palavra,(frase+posAnt+1), (c-posAnt-1));
                        }
                        palavra[c+1]='\0';
                        
                        char aux[40]={};
                        strcpy(aux, palavra);
                        for (int j = 0; j < strlen(aux); j++)//corrigindo as palavras
                        {
                            for (int k = 0; k < n; k++) //pra cada letra da palavra preciso comparar com a orig
                            {
                                if (!strncmp(orig[k], aux+j, strlen(orig[k])))
                                {
                                    strcpy(palavra+j, trad[k]); // copio trad em palavra
                                    
                                    if (strlen(aux)>= strlen(orig[k]))
                                    {
                                        int dif = strlen(aux+j+strlen(trad[k]));
                                        //printf("palavra: %s\n", palavra);
                                        //printf("resto: %s\n\n", aux+j+strlen(trad[k]));
                                        strcat(palavra, aux+j+strlen(orig[k])); // junto com o resto da palavra
                                    }
                                }     
                            }
                        } 
                        posAnt=c;
                    }
                    if(strlen(fraseTrad)&&strlen(palavra)){
                        char spc[2]= " ";
                        strcat(fraseTrad, spc); //coloco um espa�o
                    }
                    strcat(fraseTrad, palavra);
                    c++;
                }
                printf("%s\n", fraseTrad);
            }            
        }
    }
}