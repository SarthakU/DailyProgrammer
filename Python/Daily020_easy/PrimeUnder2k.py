## PRIME UNDER 2K
##
## challenge #2 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/qnkro/382012_challenge_20_easy/
## 
## 
## sarthak7u@gmail.com
##


# Counts number of prime numbers
# between 1 and num 
def primePrinter(num):
	for i in xrange(2,num):
		# remembers whether i is prime
		isPrime = True
		# checks whether i is prime by dividing all smaller numbers
		for j in xrange(2,i):
			# sets isPrime to False if found diivisible
			if i % j == 0:
				isPrime = False
		# prints i if it is prime
		if isPrim	e == True:
			print i

def main():
	primePrinter(2000)

main()
