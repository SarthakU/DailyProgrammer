/** 
 * SQUARE ROOT
 *
 * challenge #61 (intermediate)
 * http://www.reddit.com/r/dailyprogrammer/comments/uo14v/662012_challenge_61_intermediate/
 *
 * sarthak7u@gmail.com
 */
#include <iostream>
using namespace std;

double sqrt(float num);
int main()
{
	cout << "Find Squareroot of :";
	float num;
	cin >> num;
	cout << sqrt(num) 
		<<'\n';
	return 0;
}
double sqrt(float num)
{
	float high = num;
	float low = 0;
	float curr;
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