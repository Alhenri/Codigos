#include <stdio.h>
#include <stdlib.h>

int retornaUM(int a){
    return a*1;
}

int main(){

    int(*p)(int);
    p = &retornaUM;

    int numero = p(3);
    printf("%d", numero);
    
    return 0;
}