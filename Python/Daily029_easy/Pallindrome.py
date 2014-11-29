## PALLINDROME
##
## challenge #29 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/r8a70/3222012_challenge_29_easy/
## 
## 
## sarthak7u@gmail.com
def isPallindrome(word):
	return word.lower() == word[::-1].lower()