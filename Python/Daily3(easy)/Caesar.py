## CAESAR CIPHER
##
## challenge #3 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/
## 
## 
## sarthak7u@gmail.com
##

#encrypts 
def encrypt(text, key):

	cipherText = ""

	i = 0
	for letter in text:

		#skips over non-alpha characters
		if letter.isalpha() == False:
			cipherText += letter
		#ciphers using caesar cipher 
		else:
			if letter.isupper() == True:
				tempLetter = chr((ord(letter) - ord("A") + key)%26 + ord("A"))
			elif letter.islower() == True:
				tempLetter = chr((ord(letter) - ord("a") + key)%26 + ord("a"))
			cipherText += tempLetter

			
		i += 1

	return cipherText

#takes inputs from user
inputText = str(raw_input("Enter some text for me to Encrypt: "))
key = int(raw_input("Enter a key to Encrypt: "))


print encrypt(inputText, key)

raw_input()