## COUNT LINES WORDS
##
## challenge #037 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/rzdwq/482012_challenge_37_easy/
## 
## 
## sarthak7u@gmail.com
##
def count_lines(filename):
	f = open(filename, "r")
	text = f.read()
	lines = 1
	for i in text:
		if i == "\n":
			lines += 1
	print lines