#include <stdio.h>
#include <string.h>

typedef struct
{
    char nome[21]; //Nome do ninja
    char caract[21]; // caracteristica do ninja
} Ninjas;

int main(){
    int n;
    scanf("%d", &n);
    char textoAuxAnt[40];
    Ninjas ninja[n]; // Criando a struct de cada ninja

    // recebendo os dados
    for (int i = 0; i < n; i++)
    {
        char textoAux[40];
        int flag1=0;
        scanf(" %[^\n]s",textoAux); // pegando a linha inteira
        
        //Quebrar a string
        int j;
        for (j = 0; (textoAux[j]!= ' ')&&(textoAux[j]!= '\0'); j++);
        if (textoAux[j]==' '&&strcmp(textoAux, textoAuxAnt))
        {
            
            strncpy(ninja[i].nome, textoAux, j);
            ninja[i].nome[j] = '\0'; // adicionando o fim de palavra
            j++;
            strcpy(ninja[i].caract, (textoAux+j));   
        }else{
            strcpy(ninja[i].nome, "Nenhum");
            strcpy(ninja[i].caract, "Nenhuma");
        }
        strcpy(textoAuxAnt, textoAux);
    }

    // mostrando os dados
    int flag2=0;
    for (int i = 0; i < n; i++)
    {
        if (!strcmp(ninja[i].caract, "Nenhuma"))
        {
            flag2++;
        }
        
    }
    if ((n == 0)||(flag2==n))
    {
        printf("Nao havera Jounins forte esse ano");
    }
    
    else{   
        printf("Sapos:\n");
        for (int i = 0; i < n; i++)
        {
            if(!strcmp(ninja[i].caract, "Determinacao")||!strcmp(ninja[i].caract, "Coragem")||!strcmp(ninja[i].caract, "Conviccao")){
                printf("- %s\n", ninja[i].nome);
            }
        }

        printf("Cobras:\n");
        for (int i = 0; i < n; i++)
        {
            if(!strcmp(ninja[i].caract, "Ambicao")||!strcmp(ninja[i].caract, "Astucia")||!strcmp(ninja[i].caract, "Expertise")){
                printf("- %s\n", ninja[i].nome);
            }
        }

        printf("Lesmas:\n");
        for (int i = 0; i < n; i++)
        {
            if(!strcmp(ninja[i].caract, "Analise")||!strcmp(ninja[i].caract, "Suporte")||!strcmp(ninja[i].caract, "Tecnica")){
                printf("- %s\n", ninja[i].nome);
            }
        }

        printf("Macacos:\n");
        for (int i = 0; i < n; i++)
        {
            if(!strcmp(ninja[i].caract, "Agilidade")||!strcmp(ninja[i].caract, "Inteligencia")||!strcmp(ninja[i].caract, "Destreza")){
                printf("- %s\n", ninja[i].nome);
            }
        }

        printf("Caes:\n");
        for (int i = 0; i < n; i++)
        {
            if(!strcmp(ninja[i].caract, "Experiencia")||!strcmp(ninja[i].caract, "Perspicacia")||!strcmp(ninja[i].caract, "Pericia")){
                printf("- %s\n", ninja[i].nome);
            }
        }
    }
}