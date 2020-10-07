#include <stdio.h>

int main(){
    int ascii[256], c=0; // os indices serão os codigos ascii
    char aux;

    for (int i = 0; i < 256; i++)
    {
        ascii[i]=0; // zerando a contagems
    }
    while (scanf("%c", &aux)!=-1)
    {
        int auxInt = (int)aux;
        ascii[auxInt]++;//contar os caracteres    
    }
    
    for (int i = 255; i >= 0; i--)
    {
        if(ascii[i]>0){
            printf("%c %d\n", i, ascii[i]);
        }
    }
    
}