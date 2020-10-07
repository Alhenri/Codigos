#include <stdio.h>

#define max2(x, y)(x>y?x:y)// se x mauior que y retorne x, se nao retorne y

int main(){
    
    float x, y, z;
    printf("Digite x, y e z: ");
    scanf("%f %f %f", &x, &y, &z);
    printf("O maior eh: %f", max2(x, max2(y, z)));

}