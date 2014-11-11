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
char* decrypt(char* inputText, int key);

int main(void)
{
	
	int choice;
	printf("Enter 1 for encryption, 0 for decryption: ");
	scanf("%d", &choice);
	getchar();


	//reads input text to be encrypted
	char inputText[MAX_LEN] = {'\0'}; 
	printf("\nEnter some text: ");
	fgets(inputText, sizeof(inputText), stdin);

	//reads key for encryption
	int key;
	printf("\nEnter a key: ");
	scanf("%d", &key);
	getchar();
	char* outputText;
		
	switch(choice)
	{
		case 1:
			outputText = encrypt(inputText,key);
			break;
		case 0:
			outputText = decrypt(inputText,key);
			break;
		default:
			outputText = encrypt(inputText,key);
			break;
	}
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
char* decrypt(char* inputText, int key)
{
	//allocates memory for variable 
	char* text = malloc(sizeof(inputText));

	//copies contents of inputText to cipherText
	strcpy(text, inputText);

	//temporary variables
	int index = 0;

	//iterates through each char in ciphertext until null character read
	while (text[index] != '\0')
	{
		char currentChar = text[index];
		if (isalpha(currentChar) == 0)
		{}
		else
		{
			if (isupper(currentChar) == 0)
			{
				if ((int) (currentChar - key - 'a') < 0)
				{
					text[index] =  text[index]  - key + 26;			
				}
				else
				{
					text[index] =  text[index]  - key;	
				}
			}
			else
			{	
				if ((int) (currentChar - key - 'A') < 0)
				{
					text[index] =  text[index]  - key + 26;			
				}
				else
				{
					text[index] =  text[index]  - key;	
				}
			}	
		}
		index++;
	}
	return text;
}