/** 
 * DATE TO DAY IN YEAR CONVERRTER
 *
 * challenge #13 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/pzo4w/2212012_challenge_13_easy/
 *
 * sarthak7u@gmail.com
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* months[12] = {"january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"};
int dayInMonth[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		printf("Usaage: ./YearDay month day\n");
		return 1;
	}

	//Variable to store day no. in a year
	int dayNum = 0;

	//variables to store command line inputs
	char* month = argv[1];
	int day = atoi(argv[2]);

	for (int i = 0; i < 12; i++)
	{
		//adds all day if month not inputted month
		if (strcmp(month, months[i]) != 0)
		{
			dayNum += dayInMonth[i];
		}
		//adds no. of days inputted otherwise
		else
		{
			dayNum += day;
			break;
		}
	}
	printf("%d\n", dayNum);
	return 0;
}