## CAN SUM
##
## challenge #030 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/reago/3262012_challenge_30_easy/
## 
## 
## sarthak7u@gmail.com
##
def can_sum(list, target)
	i = 0
	while i < list.length
		j = i + 1
		while j < list.length
			if list[j] + list[i] == target
				return [list[i],list[j]]
			end
			j += 1
		end
		i += 1 
	end
	return "No two numbers from list sum to target"
end