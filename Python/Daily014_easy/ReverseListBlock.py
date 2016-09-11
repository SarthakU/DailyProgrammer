## Reverse List Block
##
## challenge #14 (easy)
## https://redd.it/q2v2k
##
##
## sarthak7u@gmail.com

def reverse_list_block(elems, block):
    reversed = []
    for i in xrange(0, len(elems), block):
        reversed = elems[::-1][i:i+block] + reversed
    return reversed
