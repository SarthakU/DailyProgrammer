## STAR TRIANGLE
##
## challenge #17 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/qheeu/342012_challenge_17_easy/
## 
## 
## sarthak7u@gmail.com
##
def star_triangle(height)
	height.times do |i|
		(2**i).times do 
			print "+"
		end
		print "\n"
	end
end