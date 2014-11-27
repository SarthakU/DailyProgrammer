def prime(num):
	if num == 2: return True
	elif num == 1 or num % 2 == 0: return False
	for i in xrange(3,num,2):
		if num % i == 0:
			return False
	else:
		return True