## CAESAR CIPHER
##
## challenge #3 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/
##
##
## sarthak7u@gmail.com
##

# encrypts
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

# decrypts
def decrypt(cipherText, key):
    text = ""

    i = 0
    for letter in cipherText:
        #skips over non-alpha characters
        if letter.isalpha() == False:
            text += letter
        #ciphers using caesar cipher
        else:
            if letter.isupper() == True:
                if ord(letter) - ord('A') - key < 0:
                    tempLetter = ord(letter) - key + 26
                else:
                    tempLetter = ord(letter) - key
            elif letter.islower() == True:
                if ord(letter) - ord('a') - key < 0:
                    tempLetter = ord(letter) - key + 26
                else:
                    tempLetter = ord(letter) - key
            text += chr(tempLetter)
        i += 1
    return text


# asks user whether to decrypt or encrypt then does so
choice = str(raw_input("Enter 1 for encryption, 2 for decryption: "))
if choice == "2":
    inputText = str(raw_input("Enter some text for me to Decrypt: "))
    key = int(raw_input("Enter a key to Decrypt: "))
    print decrypt(inputText, key)
else:
    inputText = str(raw_input("Enter some text for me to Encrypt: "))
    key = int(raw_input("Enter a key to Encrypt: "))
    print encrypt(inputText, key)
