## SUM THEM DIGITS 
##
## challenge #123 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/1cundw/042213_challenge_123_easy_sum_them_digits/
## 
## 
## sarthak7u@gmail.com
##
number = int(raw_input("The number please :"))
def sumThemDigits(number):
	temp = 0
	for i in xrange(len(str(number)), -1, -1):
		temp += number / 10 ** i
		number -= (number / 10 ** i) * 10 ** i
	if len(str(temp)) == 1:
		print temp
	else:
		sumThemDigits(temp)
sumThemDigits(number)
