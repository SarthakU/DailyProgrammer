/** 
 * CAESAR CIPHER
 *
 * challenge #3 (easy)
 * http://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/
 *
 * sarthak7u@gmail.com
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define MAX_LEN 30

char* encrypt(char* inputText, int key);

int main(void)
{
	
	//reads input text to be encrypted
	char inputText[MAX_LEN] = {'\0'}; 
	printf("\nEnter some text: ");
	fgets(inputText, sizeof(inputText), stdin);

	//reads key for encryption
	int key;
	printf("\nEnter a key to Encrypt: ");
	scanf("%d", &key);
	char* outputText;
	outputText = encrypt(inputText,key);
		
	//calls encrypt function and prints out results
	printf("%s\n", outputText);
	
	
}

char* encrypt(char* inputText, int key)
{
	//allocates memory for variable 
	char* cipherText = malloc(sizeof(inputText));

	//copies contents of inputText to cipherText
	strcpy(cipherText, inputText);

	//temporary variables
	int index = 0;

	//iterates through each char in ciphertext until null character read
	while (cipherText[index] != '\0')
	{
		char currentChar = cipherText[index];
		if (isalpha(currentChar) == 0)
		{}
		else
		{
			if (isupper(currentChar) == 0)
			{
				cipherText[index] =  (cipherText[index] - 'a' + key)%26 + 'a';
			}
			else
			{
				cipherText[index] =  (cipherText[index] - 'A' + key)%26 + 'A';	
			}	
		}
		index++;
	}
	return cipherText;

}
