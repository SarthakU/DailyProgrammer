/** 
 * STAR TRIANGLE
 *
 * challenge #17 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/qheeu/342012_challenge_17_easy/
 *
 * sarthak7u@gmail.com
 */

#include <iostream>

using namespace std;
int main()
{
	cout << "Enter a size of triangle : ";
	int size;
	cin >> size;
	int numberOfStars = 1;
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < numberOfStars; j++)
		{
			cout << "*";
		}
		cout << "\n";
		numberOfStars = numberOfStars *2;
	}
	return 0;
}