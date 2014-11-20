/** 
 * CHANGE CALCULATOR
 *
 * challenge #119 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/17f3y2/012813_challenge_119_easy_change_calculator/
 *
 * sarthak7u@gmail.com
 */
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	//take user input and convert to double 
	printf("Enter Amount: ");
	char amount_in_string[10];
	fgets(amount_in_string, sizeof(amount_in_string), stdin);
	double amount= strtod(amount_in_string,'\0');
	
	//multiply by 100 to make calculations easier
	amount *= 100;

	//count quarters
	int quarters = 0;
	while (amount > 25)
	{
		quarters += 1;
		amount -= 25;
	}

	//count dimes
	int dimes = 0;
	while (amount >10)
	{
		dimes += 1;
		amount -= 10;
	}

	//count nickels
	int nickels = 0;
	while (amount > 5)
	{
		nickels += 1;
		amount -= 5;
	}

	//count pennies
	int pennies = 0;
	while (amount > 0) 
	{
		pennies += 1;
		amount -= 1;
	}

	//print change required
	printf("Quarters : %d\n", quarters);
	printf("Dimes : %d\n", dimes);
	printf("Nickels : %d\n", nickels);
	printf("Pennies : %d\n", pennies);
	return 0;
}