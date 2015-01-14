## SUM THE WORD
##
## challenge #052 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/tmnfq/5142012_challenge_52_easy/
## 
## 
## sarthak7u@gmail.com
##
def sum_the_word(word)
	alpha_weight = {} # hash to represent weight of each alphabet i.e. a is 1, b is 2 etc.
	('a'..'z').to_a.each do |i|
		alpha_weight[i] = alpha_weight.length + 1
	end
	sum = 0
	word.split("").each do |i|
		sum += alpha_weight[i].to_i
	end
	return sum
end
