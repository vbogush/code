#include <stdio.h>

int main (void)
{
    int NUMBER = 0;
    printf("Please input positive int number: ");
    scanf("%d", &NUMBER);
    for(int i=0; i<NUMBER; i++)
    {   
        for(int k=NUMBER-1; k>i; k--)
        {
            printf(" ");
        }
    for(int j=0; j<i+1; j++)
    {
        printf("#");    
    }
    printf("\n");
    }   
return 0;
}