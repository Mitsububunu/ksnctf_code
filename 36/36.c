#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
  
  srand((time(NULL)) + atoi(argv[1]));

  for (int i = 0; i < 20 ; i++){
    long long r = rand();
    printf("%lld\n", r - (((r * 0x66666667 >> 32) >> 2) - (r >> 0x1f)) * 10);
    fflush(stdout);
  }
}