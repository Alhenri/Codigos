#include <stdio.h>
#include <string.h>

int main(){
    char string[300];
    char stringAux[300];
    while (scanf(" %s", stringAux)!=-1)
    {
        char spc[2]=" ";
        strcat(stringAux, spc);
        strcat(string, stringAux);
    }
    printf("%s", string);
}