## EMIRP
##
## challenge #67 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/vfylp/6222012_challenge_68_easy/
##
##
## sarthak7u@gmail.com
##

import Prime
num = int(raw_input("Enter a number: "))
emirp_list = []
for i in xrange(10,num+1):
    if Prime.prime(i):
        temp = int(str(i)[::-1])
        if Prime.prime(temp) and i != temp:
            emirp_list.append(str(i))
print ", ".join(emirp_list)
