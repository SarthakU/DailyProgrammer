## MATRIX CIPHER
##
## challenge #054 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/tux8f/5192012_challenge_54_easy/
## 
## 
## sarthak7u@gmail.com
##
def matrixCipher(text, key):
	matrix = [[]]
	for i in text:
		if len(matrix[-1]) == key:
			matrix.append([])
		matrix[-1].append(i)
	cipherText = ""
	for i in xrange(len(matrix[-1])):
		for j in matrix:
			cipherText += j[i]
	return (matrix, cipherText)
print matrixCipher("The cake is a lie!vmz", 7)