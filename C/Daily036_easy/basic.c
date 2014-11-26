#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int* numbers = malloc(sizeof(int)*20);
	for(int i = 1; i < argc; i++)
	{
		numbers[i-1] = atoi(argv[i]);
	}
	int lowest = numbers[0];
	int sum = 0;
	for(int i = 0; i < argc-1; i++)
	{
		if (lowest > numbers[i])
		{
			lowest = numbers[i];

		}
		sum += numbers[i];
	}
	sum -= lowest;
	printf("%d\n", sum);

	return 0;
}