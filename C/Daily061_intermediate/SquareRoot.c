/** 
 * SQUARE ROOT
 *
 * challenge #61 (intermediate)
 * http://www.reddit.com/r/dailyprogrammer/comments/uo14v/662012_challenge_61_intermediate/
 *
 * sarthak7u@gmail.com
 */
#include <stdio.h>

double squareroot(double num);
int main(void)
{
	printf("Find Squareroot of :");
	double num;
	scanf("%lf",&num);
	printf("%f\n", num);
	printf("%f\n", squareroot(num));
	return 0;
}
double squareroot(double num)
{
	double high = num;
	double low = 0;
	double curr;
	while ((curr*curr) - num > 0.000001 || num - (curr*curr) > 0.000001)
	{
		curr = (high + low) / 2;
		if ((curr*curr) > num)
		{
			high = curr;
		}
		else if ((curr*curr) < num)
		{
			low = curr;
		}
	}
	return curr;
}