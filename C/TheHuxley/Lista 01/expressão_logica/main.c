#include <stdio.h>

int main(){
    int a, b, c;
    char x, y;
    scanf("%d %c %d %c %d", &a, &x, &b, &y, &c);

    if(x == '^'){
        if (y=='^') // a^b^c
        {
            if (a&&b&&c)
            {
                printf("1");
            }
            else
            {
                printf("0");
            }
        }
        else // a^bvc
        {
            if (a&&b||c)
            {
                printf("1");
            }
            else
            {
                printf("0");
            }
        }
    }
    else
    {
        if (y=='^')// avb^c
        {   
            if (a||b&&c)
            {
                printf("1");
            }
            else
            {
                printf("0");
            }
        }
        else// avbvc
        {   
            if (a||b||c)
            {
                printf("1");
            }
            else
            {
                printf("0");
            }
        }
    }
    return 0;
}