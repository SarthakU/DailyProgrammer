/** 
 * STAR TRIANGLE
 *
 * challenge #17 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/qheeu/342012_challenge_17_easy/
 *
 * sarthak7u@gmail.com
 */
 
#include <stdio.h>
#include <stdlib.h>

int main()
{
	printf("Enter a size of triangle : ");
	char size[5];
	fgets(size, sizeof(size), stdin);
	int numberOfStars = 1;
	for (int i = 0; i < atoi(size); i++)
	{
		for (int j = 0; j < numberOfStars; j++)
		{
			printf("*");
		}
		printf("\n");
		numberOfStars = numberOfStars *2;
	}
	return 0;
}