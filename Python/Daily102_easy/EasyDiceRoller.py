## EASY DICE ROLLER
##
## challenge #102 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/10pf0j/9302012_challenge_102_easy_dice_roller/
##
##
## sarthak7u@gmail.com
##

import random

# take input string
string = str(raw_input("Enter your string : "))

# variables
AIndex = 0
BIndex = 0

# find at which keywords "d" and operators are stored
index = 0
for i in string:
    if i == "d":
        AIndex = index
    elif i == "-" or i == "+":
        BIndex = index
    index += 1

# compute A,B,C using indexes above found
A = string[:AIndex]
B = string[AIndex + 1: BIndex]
C = string[BIndex + 1:]
result = 0

# uses values of A,B,C to figure final result
for i in xrange(int(A)):
    result += random.randint(1,int(B)+1)
if string[BIndex] == "-":
    result = result - int(C)
elif string[BIndex] == "+":
    result = result + int(C)
print result
