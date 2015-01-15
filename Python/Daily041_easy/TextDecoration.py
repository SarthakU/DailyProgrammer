## TEXT DECORATION
##
## challenge #41 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/shp28/4192012_challenge_41_easy/
## 
## 
## sarthak7u@gmail.com
##
def text_decoration(text):
	print "*"*36
	print "*"+" "*34+"*"
	for i in xrange(0,len(text),32):
		print "* " + text[i:i+32]  +" "*(32-len(text[i:i+32])) + " *" 
	print "*"+" "*34+"*"
	print "*"*36