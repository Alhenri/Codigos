#include <stdio.h>
#include <math.h>

int main(){
    int x, y, a, b, n, m;
    scanf("(%d, %d)", &x, &y);
    scanf("%d*x^%d - %d*y^%d", &a, &n, &b, &m);

    int teste = a*pow(x, n) - b*pow(y, m);

    if (teste == 0){
        printf("a função não está definida em (%d,%d) .-.", x, y);
    } else{
        printf("a função está definida em (%d,%d)", x, y);
    }
}