## RIGHT TRIANGLE NUMBER
##
## challenge #35 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/rr4y2/432012_challenge_35_easy/
##
##
## sarthak7u@gmail.com
##

inputNum = int(raw_input("Enter a number"))
numList = []

for i in xrange(1, inputNum + 1):
    numList.append(i);
edgeSize = 1
index = -1

while True:
    if edgeSize + index > inputNum:
        break
    for i in xrange(0,edgeSize):
        index += 1
        if index >= len(numList):
            break
        print numList[index],
    print ""
    edgeSize += 1
