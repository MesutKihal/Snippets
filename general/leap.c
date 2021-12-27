#include <stdio.h>
#include <stdbool.h>
// this program checks whether or not a year is leap
int main(void){
    int year;
    bool leap = false;
    printf(">>> ");
    scanf("%d", &year);
    if (year % 4 == 0){
        leap = true;
        if (year % 100 == 0){
            leap = false;
            if (year % 400 == 0){
                leap = true;
            }
        }
    }else{
        leap = false;
        }
    if (leap == true){
        printf("True");
    }else{
        printf("False");
        } 
}
