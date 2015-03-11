## ARITHMETIC TABLES
##
## challenge #98 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/zx8vw/9152012_challenge_98_easy_arithmetic_tables/
##
##
## sarthak7u@gmail.com
##

# prints the heading row
def printFirstRow(sym, num):
    print sym, " | ",
    for i in xrange(0,num+1):
        print i,
    print ""
    line =""
    for i in xrange(0,2*(num+1+5)):
        line += "_"
    print line

# prints all rows except heading row
def printRow(numList, opNumList):
    index = 0
    for i in numList:
        print i, " | ",
        for j in opNumList[index]:
            print j,
        index += 1
        print ""
# takes required inputs from user
symbol = str(raw_input("Enter the operation: "))
num = int(raw_input("Enter a number :"))

# make list of numbers form inputted number
numbers = []
for i in xrange(0,num+1):
    numbers.append(i)

# performs operation and stores it in an array
op = []
index = 0
for i in numbers:
    op.append([])
    for j in numbers:
    # if-elif-else block to determine operation
    if symbol == "+":
        op[index].append(i+j)
    elif symbol == "*":
        op[index].append(i*j)
    elif symbol == "-":
        op[index].append(i-j)
    elif symbol == "/":
        op[index].append(i/j)
    else:
        print "operation not recognized"
        raw_input("Press enter to exit program")
        exit(1)
    index += 1

# calls print functions to print output in desired format
printFirstRow("+", num)
printRow(numbers, op)
