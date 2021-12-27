#include <stdio.h>

int main()
{
    int a;
    printf("Enter a number in decimal (base-10): ");
    scanf("%d", &a);
    int b = 1024;
    int temp = 0;
    printf("\n%d in binary (base-2) is: ", a);
    // While number a is bigger than b (1024) we keep multipling b by 2
    while (a > b){
        b *= 2;
    }
    // Converting decimal to binary
    do
    {
        temp = (int) a/b;
        a -= b*temp;
        b /= 2;
        printf("%d", temp);
    }while(b >= 1);
    return 0;
}
