## 32-BIT REVERSE
##
## challenge #67 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/vbr0z/6202012_challenge_67_easy/
## 
## 
## sarthak7u@gmail.com
##

num = bin(int(raw_input("Enter a number")))
num = num[2:]
num = num.zfill(32)
i = len(num) - 1
temp = ""
while i >= 0:
  temp += num[i]
  i -= 1
print int(temp,2)