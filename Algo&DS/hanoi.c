#include <stdio.h>

int main()
{
    int hanoi(int d, int a, int b, int c){
        if (d == 1){
            printf("move disk %d from %d to %d\n", d, a, b);
        }else{
            hanoi(d-1, a, c, b);
            printf("move disk %d from %d to %d\n", d, a, b);
            hanoi(d-1, c, b, a);
        }
    }
    hanoi(3, 0, 1, 2);
    return 0;
}
