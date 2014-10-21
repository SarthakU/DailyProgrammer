#encrypts 
def encrypt(text, key):

	cipherText = ""

	for letter in text:

		#skips over non-alpha characters
		if letter.isalpha() == False:
			cipherText += letter
		#ciphers using caesar cipher 
		else:
			cipherText += chr(ord(letter) + key)

	return cipherText

#takes inputs from user
inputText = str(raw_input("Enter some text for me to Encrypt: "))
key = int(raw_input("Enter a key to Encrypt: "))

print encrypt(inputText, key)