## challenge #9 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/pu1rf/2172012_challenge_9_easy/
## 
## 
## sarthak7u@gmail.com
#!!!!!!!!!!!! INCOMPLETE !!!!!!!!!!!!!

#list to store input digits
input_list = []

#takes input digits and adds to input_list
input = raw_input("Enter a digit:")
while 1 == 1:
	#checks if input is integer 
	try:
		input = int(input)
	except:
		input = str(input)
	
	#breaks if no input i.e. "" as input is given
	if input == "":
		break

	#makes sure only one alphabet is inputted 
	if type(input) == str:
		if len(input) != 1:
			print "Only one alphabet allowed"
		else:
			input_list.append(input)
	else:
		input_list.append(input)
	input = raw_input("Enter next digit:")

#sorts the list
input_list.sort()

#prints the list
for x in xrange(len(input_list)):
	print input_list[x]
