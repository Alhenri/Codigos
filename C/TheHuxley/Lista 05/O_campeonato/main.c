#include <stdio.h>
#include <string.h>

int main(){
    char numero[100], texto[100];
    int n;
    scanf("%s %s", numero, texto);
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++)
    {
        char teste[100];
        scanf("%s", teste);

        for (int j = 0; j < strlen(teste); j++) // cada letra dessa string
        {
            for (int k = 0; k < strlen(numero); k++)
            {
                if (teste[j]==numero[k])
                {
                    teste[j]=texto[k];
                }
            }
        }

        printf("%s\n", teste);
    }
}