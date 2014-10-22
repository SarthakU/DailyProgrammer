/** 
 * INTEREST CALCULATOR
 *
 * challenge #2 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
 *
 * sarthak7u@gmail.com
 */

#include <iostream>
#include <math.h>

using namespace std;

double simpleInterest(double principle, double rate, double timePeriod);
double compoundInterest(double principle, double rate, double timePeriod);

int main()
{
	//variables for calculation
	double principle;
	double rate;
	double timePeriod;

	cout << "Enter the Principle amount: ";
	cin >> principle; 

	cout << "Enter the interest rate: ";
	cin >> rate;

	cout << "Enter the time period: ";
	cin >> timePeriod;

	//decides whether simple or compound interest
	int choice;
	cout << "Enter 0 for simple, 1 for compounded interest\n";
	cin >> choice;

	double interest;
	switch(choice)
	{
		case 0:
			interest = simpleInterest(principle, rate, timePeriod);
			cout << "The simple interst is: " << interest;
			break;
		case 1:
			interest = compoundInterest(principle, rate, timePeriod);
			cout << "The compounded interest is : "<< interest;
			break;

	}
	return 0;
}	

/**
 * computes simple interest
 */
double simpleInterest(double principle, double rate, double timePeriod)
{
	return principle * rate * timePeriod;
}

/**
 * computes compound interest
 */
double compoundInterest(double principle, double rate, double timePeriod)
{
	return (principle * pow((1 + rate), timePeriod)) - principle;
}