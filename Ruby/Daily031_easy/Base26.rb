## BASE 26 MULTIPLICATION
##
## challenge #031 (endasy)
## http://www.reddit.com/r/dailyprogrammer/comments/rg1vv/3272012_challenge_31_easy/
## 
## 
## sarthak7u@gmail.com
##
# hash to store base 26 representation of letters
BASE_26 = Hash[("A".."Z").to_a.zip((0..25).to_a)]

# convet base 26 numbers to base 10
def base_26_to_10(num_26)
	index = num_26.length - 1
	num_10 = 0
	num_26.split("").each do |i| 
		num_10 += BASE_26[i]*(26**index)
		index -= 1
	end
	print num_10
end

def product(num1, num2)
	base_26 = Hash[("A".."Z").to_a.zip((0..25).to_a)]
	return base_26_to_10(num1)*base_26_to_10(num2)
end