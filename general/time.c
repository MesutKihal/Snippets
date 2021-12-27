#include <stdio.h>
#include <time.h>
#include <stdbool.h>
#include <unistd.h>


int main() {
    time_t current;
    while (true){
        system("clear");
        current = time(NULL);
        printf("%s", ctime(&current));
        sleep(1);
    }
    return 0;
}
