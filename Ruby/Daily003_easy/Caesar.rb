## CAESAR CIPHER
##
## challenge #3 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/
## 
## 
## sarthak7u@gmail.com
##

# returns 0 if lowercase and 1 if uppercase
# returns -1 if not alpha
def casecheck(char)

	if (char.ord >= 65 and char.ord <= 90)
		return 1
	elsif (char.ord >= 97 and char.ord <= 122)
		return 0
	else
		return -1
	end

end
		
def encrypt(text,key)

	cipherText = ""
	(text.split("")).each do |i|

		# adds character to cipher text if not num
		if casecheck(i) == -1
			cipherText += i
		# ciphers and then adds to ciphertext
		elsif casecheck(i) == 1
			cipherText += ((i.ord - 'A'.ord + key)%26 + 'A'.ord).chr
		elsif casecheck(i) == 0
			cipherText += ((i.ord - 'a'.ord + key)%26 + 'a'.ord).chr
		end

	end
	return cipherText
end

print "Enter a string to encrypt : "
text = $stdin.gets.chomp
print "Enter the key for encryption : "
key = $stdin.gets.chomp.to_i
puts encrypt(text,key)