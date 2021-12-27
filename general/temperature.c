#include <stdio.h>
#include <stdlib.h>

int main()
{
    
    
    void temperatureConvert(void){
        char answser;
        int temp;
        printf("Choose A or B\nA. Celcius to Fahrenheit\nB. Fahrenheit to Celcius\nwhat is your answser: ");
        scanf("%c", &answser);
        if (answser == 'A'){
            printf("\nEnter your temperature in Celcius: ");
            scanf("%i", &temp);
            float formula = (float) (temp*1.8) + 32;
            printf("\n%.2f F", formula);
        }else if(answser == 'B'){
            printf("\nEnter your temperature in Fahrenheit: ");
            scanf("%i", &temp);
            float formula = (float) (temp - 32) / 1.8;
            printf("\n%.2f °C", formula);
        }else{
            system("clear");
            temperatureConvert();
        }
    }
    temperatureConvert();
    return 0;
}
