## BIGGER TWO SUM
##
## challenge #34 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/rmmn8/3312012_challenge_34_easy/
## 
## 
## sarthak7u@gmail.com
import sys
numbers = [int(i) for i in sys.argv[1:]]
numbers.remove(min(numbers))
print sum(numbers)