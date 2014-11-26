## GREATEST COMMON DIVISER
##
## challenge #132 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/1hvh6u/070813_challenge_132_easy_greatest_common_divisor/
## 
## 
## sarthak7u@gmail.com
##
def greatest_common_diviser(num1, num2)	
	num = [num1,num2].min
	(1..num).reverse_each do |i|
		if num1 % i == 0 and num2 % i == 0
			return i
		end
	end
end
def main
	print "Enter first number: "
	num1 = $stdin.gets.chomp.to_i
	
	print "Enter second number: "
	num2 = $stdin.gets.chomp.to_i
	
	print "\nGreatest common diviser of "
	print "#{num1} and #{num2} is "
	puts "#{greatest_common_diviser(num1,num2)}"
end
main