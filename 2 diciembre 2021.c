#include <stdio.h>

int main()
{
    int valor = 0;
    printf("Dame un valor entero:");
    scanf("%1",&valor);
    while(valor !=0){
        printf("%i \n",valor);
        printf("Dame un valor entero;");
        scanf("%i",&valor);
    }
    printf("Fin del programa");
    return 0;
}
