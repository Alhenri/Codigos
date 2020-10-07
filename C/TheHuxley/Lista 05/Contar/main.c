#include <stdio.h>
#include <string.h>

int main(){
    char string[1000], substring[1000];
    int flagSub=0, countSub=0;

    scanf("%[^\n]s", string);
    scanf("%s", substring);

    for (int i = 0; i < strlen(string); i++)
    {
        if(string[i]==substring[0]){ // começo da substring
            flagSub=1; // digamos que achei a substring
            
            for (int j = 0; j < strlen(substring); j++) // contra prova
            {
                if (string[i+j]!=substring[j])// caso alguma letra seja diferente
                {
                    flagSub=0; // Vejo que não é uma substring
                }
            }
            
            countSub+=flagSub;
        }
    }

    printf("%d", countSub);
    
}