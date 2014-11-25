## Morse
##
## challenge #7 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/
## 
## 
## sarthak7u@gmail.com
import string
import sys

morse = [".-", "-...", "-.-.","-..",".","..-.", "--.", "....","..",
			".---","-.-",".-..","--","-.", "---", ".--.", "--.-", ".-.",
			"...","-","..-","...-",".--", "-..-","-.--","--.."]
alpha = list(string.ascii_lowercase)

def morse_to_alpha(alpha,morse):
	letters_in_morse = [""]
	user_input = raw_input("Enter a string in morse: ")

	for i in user_input:
		if i == " ":
			letters_in_morse.append("")
			continue
		letters_in_morse[-1] += i 

	# makes a dictionary for morse to alpha
	morse_to_alpha = dict(zip(morse,alpha))
	morse_to_alpha["/"] = " "

	output =[morse_to_alpha[j] for j in letters_in_morse]
	print "".join(output)

def alpha_to_morse(alpha,morse):
	user_input = raw_input("Enter a string in alpha : ")

	# makes a dictionary for alpha to morse
	alpha_to_morse = dict(zip(alpha,morse))
	alpha_to_morse["/"] = " "

	output =[alpha_to_morse[j] for j in user_input]
	print " ".join(output)

# Ask user which type of conversion
choice = int(raw_input("""
Enter 0 for morse to alpha or 
Enter 1 for alpha to morse:\n"""))

if choice == 0:
	morse_to_alpha(alpha,morse)
elif choice == 1:
	alpha_to_morse(alpha,morse)