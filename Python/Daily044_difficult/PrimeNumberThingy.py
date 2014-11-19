## PRIME NUMBER THINGY
##
## challenge #44 (difficult)
## http://www.reddit.com/r/dailyprogrammer/comments/srp5q/4252012_challenge_44_difficult/
## 
## 
## sarthak7u@gmail.com
##

from sys import argv
lower_limit = int(argv[1]);upper_limit = int(argv[2]) + lower_limit
prime_list = []
prime_sum = 0
count = 0
j = 0
for i in xrange(lower_limit,upper_limit):
    is_prime = True
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        is_prime = False
    else:
        for j in xrange(11, i, 2):
            if i % j == 0:
                is_prime = False
                break
            count += 1
    if is_prime == True:
        prime_list.append(i)
        prime_sum += i
print prime_sum
#print prime_list
print len(prime_list)
print "----------",count,"----------"