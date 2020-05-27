#include <stdio.h>
#include <stdlib.h>

int main(){
    char frase[9];
    for(int x = 0; x<9; x++){
        scanf("%c", &frase[x]);
        if((int)frase[x] == 10){
            x--;
        }
    }
    printf("=-=-=-=-=-=-=-=-=-=-\n");
    for (int i = 0; i < 9; i++)
    {
        printf("%c", frase[i]);
    }
    
    return 1;
}