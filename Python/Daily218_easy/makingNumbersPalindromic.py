## MAKING NUMBERS PALINDROMIC
##
## challenge #218 (easy)
## https://www.reddit.com/r/dailyprogrammer/comments/38yy9s/20150608_challenge_218_easy_making_numbers/
##
##
## sarthak7u@gmail.com

def making_number_palindromic(num):
    original = num
    steps = 0
    while str(num)[::-1] != str(num):
        num += int(str(num)[::-1])
        steps += 1
    print original, "gets palindromic after", steps, "steps:", num
