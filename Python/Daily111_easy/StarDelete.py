## STAR DELETE
##
## challenge #111 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/12qi5b/1162012_challenge_111_easy_star_delete/
##
##
## sarthak7u@gmail.com

import sys

# takes string as input
# returns string with star along with its trailing and leading element removed
def starDelete(inputString):
    starlessList = inputString.split("*")
    index = 0
    while index < len(starlessList):
        # handle first and last stars
        if index != len(starlessList) - 1:
            starlessList[index] = starlessList[index][:-1]
        if index != 0:
            starlessList[index] = starlessList[index][1:]
        index += 1
    return "".join(starlessList)

def main():
    if len(sys.argv) != 2:
        print "Usage StarDelete.py stringwithstar"
        return 1
    inputString = sys.argv[1]
    print starDelete(inputString)
main()
