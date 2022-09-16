#include <stdio.h>

int main(void){
	
	
	double myDoubles[] = {0.2, 1.4, 2.5, 3.3, 4.9}; 
	double *pi = myDoubles;
	for(int counter = 0; counter < 5; counter++){
		printf("Address %p: Value %f\n", pi, *pi);
		pi += 1;
	}
	char myChars[] = {'J', 'o', 'h', 'n'}; 
	char *pi2 = myChars;
	for(int counter = 0; counter < 4; counter++){
		printf("Address %p: Value %c\n", pi2, *pi2);
		pi2 += 1;
	}
}
/*
 * Suppose you had no other way to find out the size of an int, a 
 * double, or a byte (and note that, in C, these may actually vary 
 * between different compilers!)  How could the output from your 
 * program help you answer these questions?
 * 
 * 
 **/
