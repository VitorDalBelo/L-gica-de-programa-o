#include <stdio.h>
int analisar(char l){
	int aux=l;
	return l>='a' && l<='z';
}

void main (void){
	char letra;
	printf("Insira uma letra\n");
	scanf("%c",&letra);
	if(analisar(letra)){
		printf("Valor dentro do intervalo a-z");
	}
	else{
		printf("Valor fora do intervalo a-z");
	}
	
}
