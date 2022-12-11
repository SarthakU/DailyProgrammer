## DUPLICATE STRING 
##
## challenge #26 (easy)
## https://www.reddit.com/r/dailyprogrammer/comments/qzil1/3162012_challenge_26_easy/ 
##
##
## sarthak7u@gmail.com
##

def removeDupes(string):
    unique = ""
    remainder = ""
    prev = ""
    for i in string:
        if prev != i:
            unique += i
        else:
            remainder += i
        prev = i
    print(unique, remainder)        


if __name__ == "__main__":
    removeDupes("balloons") 
    removeDupes("ddaaiillyypprrooggrraammeerr") 
    removeDupes("aabbccddeded") 
    removeDupes("flabby aapples") 
