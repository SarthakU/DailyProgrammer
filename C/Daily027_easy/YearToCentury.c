/** 
 * YEAR TO CENTURY
 *
 * challenge #27 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/r0r3h/3172012_challenge_27_easy/
 *
 * sarthak7u@gmail.com
 */

#include <stdio.h>

int isLeapYear(int year);

int main(int argc, char const *argv[])
{
	// takes input year
	int year;
	printf("Enter Year :");
	scanf("%d", &year);

	// prints century
	printf("Century : %d\n", (year/100+1));
	
	//prints whether leap year on not
	int leapYear = isLeapYear(year);
	printf("Leap Year : ");
	switch (leapYear)
	{
		case 0:
			printf("Yes\n");
			break;
		case 1:
			printf("No\n");
	}
	return 0;
}


/*
 * Checks whether year is leap year
 * returns 0 if year is leap year
 * returns 1 otherwise
 */
int isLeapYear(int year)
{
	if (year % 4 != 0)
	{
		return 1;
	}
	else
	{
		if (year % 100 == 0)
		{
			if (year % 400 != 0)
			{
				return 1;
			}
		}
	}
	return 0;
}