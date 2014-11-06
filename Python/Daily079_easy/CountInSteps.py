## COUNTING IN STEPS
##
## challenge #79 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/wvc21/7182012_challenge_79_easy_counting_in_steps/
## 
## 
## sarthak7u@gmail.com
##

def step_count(start, stop, steps):
	arr = [float(start)]
	inc = (stop - start) / (steps)
	for i in xrange(0,steps):
		start += inc
		arr.append(round(float(start)))
	return arr
print step_count(-5.75, 12.00, 5)
