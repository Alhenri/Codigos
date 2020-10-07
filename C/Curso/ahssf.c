#include<stdio.h>

int main(){

	int soma=0;
    int n;

	do{
		printf("Digite um numero (menor que 0 para parar):");
		scanf("%d",&n);

		if(n>0)soma=soma+n;
	
    }while(n>0);

	printf("Total: %d", soma);

	return 0;

}