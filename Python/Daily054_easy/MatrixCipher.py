## MATRIX CIPHER
##
## challenge #054 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/tux8f/5192012_challenge_54_easy/
## 
## 
## sarthak7u@gmail.com
##
def matrixCipher(text, key):
	import random
	#make the matrix
	matrix = [[]]
	for i in text:
		if len(matrix[-1]) == key:
			matrix.append([])
		matrix[-1].append(i)
	while len(matrix[-1]) != len(matrix[0]):
		matrix[-1].append(chr(random.randint(97,122)))
	#make matrix in to text
	cipherText = ""
	for i in xrange(len(matrix[-1])):
		for j in matrix:
			cipherText += j[i]
	return cipherText
def decryptMatrixCipher(text):
	'''can decrypt matrix cipher if 
	the message starts with "It seems"'''
	testText = "It_seems"
	key = 0
	#find the key
	for i in xrange(1,len(text)):
		if text[0::i][:len(testText)] == testText:
			key = i 
			break
	#figure text using key found above
	messageText = ""
	if key == 0:
		print "Sorry! I can't crack this cipher at this time!"
		return 1
	for i in xrange(0,key):
		messageText += text[i::key]
	return (key,messageText)