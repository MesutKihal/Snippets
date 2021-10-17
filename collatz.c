#include <stdio.h>
// This program will generate all the terms of the collatz conjecture
int main(void)
{
    int i;
    scanf("%d", &i);
    do{
        if (i%2==0){
            i /= 2;
        }else{
            i = (i * 3)+1;
        }
        printf("%d\n", i);
    }
    while (i!=1);

    return 0;
}
