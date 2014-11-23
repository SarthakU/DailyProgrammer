## REVERSED STRING
##
## challenge #13 (intermediate)
## http://www.reddit.com/r/dailyprogrammer/comments/pzo7g/2212012_challenge_13_intermediate/
## 
## 
## sarthak7u@gmail.com
##
string = list(raw_input("Enter String:"))
string.reverse()
open("reverse.txt", "w").write("".join(string))