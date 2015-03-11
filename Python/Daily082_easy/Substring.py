## SUBSTRING
##
## challenge #82 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/x8rl8/7272012_challenge_82_easy_substring_list/
##
##
## sarthak7u@gmail.com
##

import string
number = int(raw_input("Enter number :"))
alphabet = string.ascii_lowercase
substring = alphabet[:number]

for i in substring:
    temp = ""
    for j in substring[substring.index(i):]:
        temp += j
        print temp
