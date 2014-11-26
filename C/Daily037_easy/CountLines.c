/** 
 * COUNT LINES 
 *
 * challenge #37 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/rzdwq/482012_challenge_37_easy/
 *
 * sarthak7u@gmail.com
 */
#include <stdio.h>

int main(int argc, char *argv[])
{
	// check if filename is inputted
	if (argc != 2)
	{
		printf("Usage : ./count file \n");
		return 1;
	}
	char* infile = argv[1];
	
	// checks whether file exists
	FILE* inptr = fopen(infile, "r");
	if (inptr == NULL)
	{
		printf("Could not open %s\n", infile);
		return 2;
	}

	// variables
	int lines = 1;
	int words = 1;

	// reads file character by character
	char buffer;
	while (fread(&buffer, sizeof(buffer), 1, inptr) != 0)
	{
		if (buffer == '\n')
		{
			lines ++;
			words ++;
		}
		else if (buffer == ' ')
		{
			words ++;
		}
	}

	// closes the file
	fclose(inptr);

	printf("Number of words : %d\n", words);
	printf("Number of lines : %d\n", lines);
	return 0;
}