## CROP BINARY MATRIX
##
## challenge #73 (intermediate)
## http://www.reddit.com/r/dailyprogrammer/comments/w4ma2/762012_challenge_73_intermediate/
##
##
## sarthak7u@gmail.com
##

def crop_bin_matric(ascii_matrix):
    for i in xrange(len(ascii_matrix)-1, -1, -1):
        if ascii_matrix[i].count('0') == len(ascii_matrix[i]):
            ascii_matrix.pop(i)
    index = 0
    while index < len(ascii_matrix[0]):
        all_zero = True
        for i in ascii_matrix:
            if i[index] != "0":
                all_zero = False
                break
        if all_zero:
            ascii_matrix = [i[:index] + " " + i[index+1:] for i in ascii_matrix]
        index += 1
    ascii_matrix = [i.strip() for i in ascii_matrix]
    return "\n".join(ascii_matrix)
