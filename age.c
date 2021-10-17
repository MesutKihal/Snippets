#include <stdio.h>
#include <cs50.h> 
// This program tells you when will you turn 100 years old
int main(void)
{
    string name = get_string("Enter your name: ");
    int age = get_int("Enter your age: ");
    int future = (2021-age)+100;
    printf("%s will turn 100 years old in %d\n", name, future);
}
