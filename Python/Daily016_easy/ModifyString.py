## MODUFY STRING
##
## challenge #016 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/q8aom/2272012_challenge_16_easy/
## 
## 
## sarthak7u@gmail.com
##
def modify_string(string, remove_chars):
	modified = ""
	for i in string:
		if i not in remove_chars:
			modified += i
	return modified