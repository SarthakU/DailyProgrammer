## REVERSE POLISH NOTATION (RPN)
##
## challenge #38 (intermediate)
## http://www.reddit.com/r/dailyprogrammer/comments/s2na8/4102012_challenge_38_intermediate/
## 
## 
## sarthak7u@gmail.com
##

inputExp = str(raw_input("Enter an expression"))
rpn = []
operators = []  # list to store operators not yet added in rpn
for i in inputExp:
	if i == "(":
		pass
	elif i.isalpha() == True:
		rpn.append(i)
	elif i == "*" or i == "+" or i == "-" or i == "/" or i == "^":
		operators.append(i)
	elif i == ")":
		rpn.append(operators.pop())

print "".join(rpn)