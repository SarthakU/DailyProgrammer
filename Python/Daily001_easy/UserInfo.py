## USER INFO
##
## challenge #1 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
## 
## 
## sarthak7u@gmail.com
name = raw_input("What is you name: ")

age = raw_input("What is your age :")

username = raw_input("What is your reddit username: ")

print "your name is " + name +", you're " + age + " years old"
print ", and your user name is" + username

open("userinfo.txt","a").write(name + " " + age + " " + username + "\n")