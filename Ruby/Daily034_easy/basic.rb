## BIGGER TWO SUM
##
## challenge #34 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/rmmn8/3312012_challenge_34_easy/
## 
## 
## sarthak7u@gmail.com
numbers = []
sum = 0
ARGV.each {|i| numbers.push(i.to_i); sum+=i.to_i }
min = numbers.delete(numbers.min)
puts sum - min