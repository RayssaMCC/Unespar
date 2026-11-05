#include <stdio.h>
#include <stdlib.h>

main(){
	int r;
	printf("Escolha um animal entre:\n Leao\n Cavalo\n Homem\n Macaco\n Morcego\n Baleia\n Avestruz\n Pinguim\n Pato\n Aguia\n Tartaruga\n Crocodilo\n Cobra \n\n");
	printf("Responda com 1 para sim e 0 para nao as perguntas a seguir. \n\n");
	
	printf("E mamifero? ");
	scanf("%d", &r);
	
	//Mamiferos
	if (r == 1){
		printf("E quadrupede? ");
		scanf("%d", &r);
		//Quadrupedes
		if (r == 1){
			printf("E carnivoro? ");
			scanf("%d", &r);
			//Carnivoros
			if (r == 1){
				printf("Entao o animal escolhido foi o leao");
			}//fecha chave de leao
			
			else if (r == 0) {
				printf("E herbivoro? ");
				scanf("%d", &r);
				//Herbivoros
				if (r == 1){
					printf("Entao o animal escolhido foi o cavalo");
				}//fecha chave de cavalo
			}
			
		}else if (r == 0){
			printf("E bipede? ");
			scanf("%d", &r);
			//Bipedes
			if (r == 1){
				printf("E onivoro? ");
				scanf("%d", &r);
				if (r == 1){
					printf("Entao o animal escolhido foi o homem");
				}//fecha chave de homem
				
				else if (r == 0){
					printf("E frugivoro? ");
					scanf("%d", &r);
					//Frugivoros
					if (r == 1){
						printf("Entao o animal escolhido foi o macaco");
					}//fecha chave de macaco
				}
				
			} else if (r == 0) {
				printf("E voador? ");
				scanf("%d", &r);
				//Voadores
				if (r == 1){
					printf("Entao o animal escolhido foi o morcego");
				}//fecha chave de morcego

				else if(r == 0){
					printf("E aquatico? ");
					scanf("%d", &r);
					//Aquaticos
					if (r == 1){
						printf("Entao o animal escolhido foi a baleia");
					}// fecha chave de baleia
				}
			}
		}
	} 
	else if (r == 0){
		printf("E uma ave? ");
		scanf("%d", &r);
		//Aves
		if (r == 1){
			printf("E nao-voadora? ");
			scanf("%d", &r);
			//Nao-voadoras
			if (r == 1){
				printf("E tropical? ");
				scanf("%d", &r);
				//Tropicais
				if (r == 1){
					printf("Entao o animal escolhido foi o avestruz");
				}//fecha chave do avestruz
				
				else if ( r == 0){
					printf("E polar? ");
					scanf("%d", &r);
					//Polares
					if (r == 1){
						printf("Entao o animal escolhido foi o pinguim");
					}//fecha chave do pinguim
				}
			} else if (r == 0){
				printf("E nadadora? ");
				scanf("%d", &r);
				//Nadadoras
				if (r == 1){
					printf("Entao o animal escolhido foi o pato");
				}//fecha chave de pato
				
				else if (r == 0){
					printf("E de rapina? ");
					scanf("%d", &r);
					//De rapina
					if (r == 1){
						printf("Entao o animal escolhido foi a aguia");
					}//fecha chave de aguia	
				}
			}
		}
  		else if ( r == 0){
			printf("E um reptil? ");
			scanf("%d", &r);
			//Reptil
			if ( r == 1){
				printf("Possui casco? ");
				scanf("%d", &r);
				//Casco
				if (r == 1){
					printf("Entao o animal escolhido foi a tartaruga");
				}//fecha chave de tartaruga
				
				else if (r == 0){
					printf("E carnivoro? ");
					scanf("%d", &r);
					//Carnivoro
					if (r == 1){
						printf("Entao o animal escolhido foi o crocodilo");
					}//fecha chave de crocodilo
					
					else if (r == 0){
						printf("Sem patas? ");
						scanf("%d", &r);
						//Sem patas
						if (r == 1){
							printf("Entao o animal escolhido foi a cobra");
						}
					}
				}
			}
		}
	} 
	printf("\n");
	system("pause");
}

