#include <stdio.h>

int main (void)
{
    int NUMBER = 0;
    printf("Please input int number: ");

    scanf("%d", &NUMBER);

    if(NUMBER <= 0)
    {
        printf("Please input positive int\n");
        return 1;
    }
    else
    {
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
    printf(" ");
    for(int l=0; l<i+1; l++)
    {
        printf("#");    
    }
    printf("\n");
    }  
    } 
return 0;
}