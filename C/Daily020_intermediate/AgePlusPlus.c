/** 
 * AGE PLUS PLUS
 *
 * challenge #20 (intermediate)
 * http://www.reddit.com/r/dailyprogrammer/comments/qnkpp/382012_challenge_20_intermediate/
 *
 * sarthak7u@gmail.com
 */
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char const *argv[])
{
	char age_string[4];
	printf("How old are you? ");
	fgets(age_string,sizeof(age_string), stdin);
	int age = atoi(age_string);

	printf("Months  : %d\n", age*12);
	printf("Days    : %d\n", age*12*30);	
	printf("Hours   : %d\n", age*12*30*24);
	printf("Minutes : %d\n", age*12*30*24*60);
	return 0;
}