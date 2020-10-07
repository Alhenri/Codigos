#include <stdio.h>
#include <string.h>

int main(){
    char dados[10000][15]={};
    int flag=1;

    while (flag)
    {
        char command[8]={}, aux[15]={};
        int id;
        scanf(" %s\n", command);

        if(!strcmp(command, "POST")){ // POST
            scanf("%d %s\n", &id, aux);
            int cont=0;
            for (int i = 0; i < 10000; i++)
            {
                if(strlen(dados[i])>0){
                    cont++;
                }
            }
            if (cont>=100) // se tiver algo ele nao pode criar
            {
                printf("Banco cheio!\n");
            }
            else
            {
                strcpy(dados[id], aux);
                printf("Adicionado: %d %s\n", id, dados[id]);
            }
        }else

        if(!strcmp(command, "PUT")){ // PUT
            scanf("%d %s\n", &id, aux);
            if (strlen(dados[id])>0)
            {
                strcpy(dados[id], aux);
                printf("Atualizado: %d %s\n", id, aux);
            }
            else // se nao tiver nada não pode atualizar
            {
                printf("ID não encontrado!\n");
            }
        }else
        
        if(!strcmp(command, "DELETE")){ // DELETE
            scanf("%d\n", &id);
            if (strlen(dados[id])>0)
            {
                printf("Excluido: %d %s\n", id, dados[id]);
                strcpy(dados[id], ""); // excluo
            }else
            {
                printf("ID não encontrado!\n");
            }
        }else
        
        if(!strcmp(command, "GET")){ // GET
            scanf("%d", &id);
            if (strlen(dados[id])>0)
            {
                printf("Enviado: %d %s\n", id, dados[id]);
            }else
            {
                printf("ID não encontrado!\n");
            }
        }
        
        else // CLOSE
        {
            printf("Dados no banco:\n");
            for (int i = 0; i < 10000; i++)
            {
                if(strlen(dados[i])>0){
                    printf("%d %s\n", i, dados[i]);
                }
            }
            
            flag=0;
        }
    }
}