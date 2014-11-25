## USER INFO
##
## challenge #1 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
## 
## 
## sarthak7u@gmail.com
print "What is you name: "
name = $stdin.gets.chomp

print "What is your age :"
age = $stdin.gets.chomp

print "What is your reddit username: "
username = $stdin.gets.chomp

print "\nyour name is #{name}, you're #{age} years old"
print ", and your user name is #{username}\n"

open("userinfo.txt","a").write("#{name} #{age} #{username}\n")