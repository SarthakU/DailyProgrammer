/** 
 * REVERSE STRING
 *
 * challenge #13 (intermediate)
 * http://www.reddit.com/r/dailyprogrammer/comments/pzo7g/2212012_challenge_13_intermediate/
 *
 * sarthak7u@gmail.com
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* revstring(char* string)
{
	char* reverse_string = (char*) malloc(strlen(string)*sizeof(char));
	int index = 0;
	for (int i = strlen(string)-1; i >= 0; i--)
	{	
		reverse_string[index] = string[i];
		index ++;
	}
	reverse_string[index] = '\0';
	return reverse_string;
}