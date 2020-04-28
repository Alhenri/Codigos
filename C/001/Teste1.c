#include <stdlib.h>
#include <stdio.h>
int main(int argc, char *argv[]){
    float x, r;
	printf("Digite um numero: ");
	scanf("%f", &x);
	printf("%f\n", x);
	r =((5*x*x*x)-(49*x*x)+(118*x))/8;
	printf("Valor retornado: %f\n", r);
	return 0;
}