## NEXT HIGHER
##
## challenge #021 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/qp3ub/392012_challenge_21_easy/
##
##
## sarthak7u@gmail.com
##

def diff_digits(num):
    num = str(num)
    digits = []
    for i in num:
        if i not in digits:
            digits.append(i)
    return sorted(digits)

def next_higher(num):
    next_higher = num + 1
    while diff_digits(num) != diff_digits(next_higher):
        next_higher += 1
    return next_higher
