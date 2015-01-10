def sum_the_word(word)
	alpha_weight = {} # hash to represent weight of each alphabet i.e. a is 0, b is 1 etc.
	('a'..'z').to_a.each do |i|
		alpha_weight[i] = alpha_weight.length
	end
	sum = 0
	word.each do |i|
		sum += alpha_weight[i]
	end
	return sum
end
sum_the_word(1)