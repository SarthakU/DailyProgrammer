## SQUARE ROOT
##
## challenge #061 (intermediate)
## http://www.reddit.com/r/dailyprogrammer/comments/uo14v/662012_challenge_61_intermediate/
##
##
## sarthak7u@gmail.com
##

def sqrt(num):
    high = float(num)
    low = 0
    curr = (num+low)/2
    while (curr*curr) - num > 0.000001 or num - (curr*curr) > 0.000001:
        curr = (high+low)/2
        if (curr*curr) > num:
            high = curr
        elif curr < num:
            low = curr
    return round(curr,6)
num = float(raw_input("Find Squareroot of :"))
print sqrt(num)
