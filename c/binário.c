#include <stdio.h>

//este coódigo faz uma conversao de base de  decimal para binario
int main(void){
	
	int i,a,q;
	int num;
	printf("Entre com um numero inteiro:");
	scanf("%d",&num);
	int tam=32; 
	int vet[tam];
	
	for(q=0;q<tam;q++){// garante que não havera lixo de momória no resultado
		vet[q]=0;
	}
	for(a=tam-1;a>=0;a--){//Calcula e atribui ao vetor os resultados
		printf("num e %d \n",num);
        if(num == 1){
        	printf("estou pondo %d na caixa %d \n CHRGOU NO IF\n",num,a);
        	vet[a]=num;
        	break;
		}
		else{
		vet[a]=num%2;
		num/=2;
		printf("estou pondo %d na caixa %d \n",num%2,a);
		}
	}
	
	for(i = 0;i<tam;i++){//Imprime
		printf("%d",vet[i]);
	}
	return 0;
}
