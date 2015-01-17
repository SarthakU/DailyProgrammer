## BOGOSORT
##
## challenge #34 (intermediate)
## http://www.reddit.com/r/dailyprogrammer/comments/rmmqx/3312012_challenge_34_intermediate/
## 
## 
## sarthak7u@gmail.com
##
import random
def bogo_sort(num_list):
	while num_list != sorted(num_list):
		random.shuffle(num_list)
	return num_list