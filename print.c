#include <stdio.h>

int main(int argc, char * argv[]){
int NUMBER = 5;
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