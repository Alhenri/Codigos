#include <stdio.h>
#include <string.h>

int main(){
    char saidaI[1000]={}, mov[4]={};

    while (scanf("%s", mov)!=-1)
    {
        int flagAnt=0, flag180=0;
        if (mov[1]==39)
        {
            flagAnt=1;
        }
        if(mov[1]=='2'){
            flag180=1;
        }
        
        switch (mov[0])
        {
        case 'U':

            if (flagAnt) // Se for um antihorario vira horario
            {
                strcpy(mov, "U ");
            }else
            if(!flag180){ // Se não for um horario vira antihorario
                strcpy(mov, "U' ");
            }
        
            break;
        case 'D':
            
            if (flagAnt) // Se for um antihorario vira horario
            {
                strcpy(mov, "D ");
            }else
            if(!flag180){ // Se não for um horario vira antihorario
                strcpy(mov, "D' ");
            }

            break;
        case 'R':

            if (flagAnt) // Se for um antihorario vira horario
            {
                strcpy(mov, "R ");
            }else
            if(!flag180){ // Se não for um horario vira antihorario
                strcpy(mov, "R' ");
            }

            break;
        case 'L':

            if (flagAnt) // Se for um antihorario vira horario
            {
                strcpy(mov, "L ");
            }else
            if(!flag180){ // Se não for um horario vira antihorario
                strcpy(mov, "L' ");
            }

            break;
        case 'F':

            if (flagAnt) // Se for um antihorario vira horario
            {
                strcpy(mov, "F ");
            }else
            if(!flag180){ // Se não for um horario vira antihorario
                strcpy(mov, "F' ");
            }

            break;
        case 'B':
            
            if (flagAnt) // Se for um antihorario vira horario
            {
                strcpy(mov, "B ");
            }else
            if(!flag180){ // Se não for um horario vira antihorario
                strcpy(mov, "B' ");
            }

            break;
        default:
            break;
        }

        if (flag180)
        {
            strcat(mov, " ");
        }
        strcat(saidaI, mov);
    }
    
    for (int i = strlen(saidaI); i >= 0; i--)
    {
        if (saidaI[i-1]==' '||saidaI[i]==' '||i==0)
        {
            printf("%c", saidaI[i]);
        }else
        {
            printf("%c%c", saidaI[i-1], saidaI[i]); // reinverte 
            i--;  
        }
    }
}