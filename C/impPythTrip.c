#include <stdio.h>
#include <math.h>

double triples[3][3];
void inputTwoSides(double sideA, double sideB, int rowIndex){
	double hyp = sqrt(pow(sideA, 2) + pow(sideB, 2));
	triples[rowIndex][0] = sideA;
	triples[rowIndex][1] = sideB;
	triples[rowIndex][2] = hyp;
}

void inputOneSideAndHyp(double sideA, double hyp, int rowIndex) {
	double sideB = sqrt(pow(hyp, 2) - pow(sideA, 2));
	triples[rowIndex][0] = sideA;
	triples[rowIndex][1] = sideB;
	triples[rowIndex][2] = hyp;
}
int main(void){
	inputOneSideAndHyp(3, 5, 0);
	inputOneSideAndHyp(1, sqrt(2), 1);
	inputTwoSides(2, 3, 2);
	for (int i =0;i<3;i++)
		printf("PythTriple [sideA = %5.3f, sideB = %5.3f, hyp = %5.3f]\n"
		,triples[i][0],triples[i][1],triples[i][2]);
}	
