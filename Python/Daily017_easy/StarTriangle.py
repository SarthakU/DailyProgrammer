## STAR TRIANGLE
##
## challenge #17 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
##
##
## sarthak7u@gmail.com

size = int(raw_input("Enter a size of triangle : ")) ; numberOfStars = 1
for i in xrange(0, size):
    for j in xrange(0,numberOfStars):
        print "*",
    numberOfStars *= 2
    print ""
