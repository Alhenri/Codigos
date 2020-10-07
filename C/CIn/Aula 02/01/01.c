#include <stdio.h>
#include <math.h>

int main(){
    float Xa, Xb, Ya, Yb, Za, Zb;
    printf("Digite as cordenadas 'X Y Z' do ponto A: ");
    scanf("%f %f %f", &Xa, &Ya, &Za);

    printf("Digite as cordenadas 'X Y Z' do ponto B: ");
    scanf("%f %f %f", &Xb, &Yb, &Zb);

    float dist = sqrt(pow(Xa-Xb, 2)+pow(Ya-Yb, 2)+pow(Za-Zb, 2));
    printf("A distancia eh: %.2f", dist);

    return 0;
}