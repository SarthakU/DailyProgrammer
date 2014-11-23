## REVERSED STRING
##
## challenge #13 (intermediate)
## http://www.reddit.com/r/dailyprogrammer/comments/pzo7g/2212012_challenge_13_intermediate/
## 
## 
## sarthak7u@gmail.com
##
string = raw_input("Enter String:")
open("reverse.txt", 'w').write(string[::-1])