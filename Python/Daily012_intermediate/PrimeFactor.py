## PRIME FACTOR
##
## challenge #12 (intermediate)
## http://www.reddit.com/r/dailyprogrammer/comments/pxrzh/2202012_challenge_12_intermediate/
## 
## 
## sarthak7u@gmail.com
def prime_factor(num):
	import Prime
	prime_factor_list = []
	factor = 2
	while num != 1:
		if not Prime.prime(factor) :
			factor += 1
			continue
		if num % factor != 0:
			factor += 1
			continue
		else:
			num = num / factor
			prime_factor_list.append(factor)
	return prime_factor_list
def main():
	num = int(raw_input("Enter a number: "))
	print "\n", num, "=",
	for i in prime_factor(num)[:-1]: 
		print i, "*",
	print prime_factor(num)[-1]
main()