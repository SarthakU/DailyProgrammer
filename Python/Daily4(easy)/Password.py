## PASSWORD GENERATOR
##
## challenge #4 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
## 
## 
## sarthak7u@gmail.com

import string
import random

#list of the alphabets
alphabets = list(string.ascii_lowercase) 

#list to store passwords
passwords = []

#no of passwords to generete
numPasswords = raw_input("Enter number of passwords to be genereted:")

#sets no of passwords to 1 if user fails to 
if numPasswords == "":
	numPasswords = 1

for x in xrange(int(numPasswords)):		
	#gets length of password from user
	passwordLength = raw_input("Enter length of password: ")

	#randomly generates password length if user doesn't provide
	if passwordLength == '':
		passwordLength = random.randint(8,11)

	#randomly selects an alphabet from alphabets for each position
	password = ""
	for i in xrange(int(passwordLength)):
		password += alphabets[random.randint(0,25)]

	#adds password to list of pass words
	passwords.append(password)

#prints passwords
for password in passwords:
	print password