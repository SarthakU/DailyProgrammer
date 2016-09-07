## Morse
##
## challenge #169 (easy)
## https://redd.it/29i9jw
##
##
## sarthak7u@gmail.com

TEST_TEXT = '''1 2 3 4 5 6 7 8 9 0
0 9 8 7 6 5 4 3 2 1
1 3 5 7 9 2 4 6 8 0
0 8 6 4 2 9 7 5 3 1
0 1 2 3 4 5 4 3 2 1
9 8 7 6 5 6 7 8 9 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
9 8 7 6 7 8 9 8 7 6
0 0 0 0 0 0 0 0 0 0'''

def parse_matrix(text):
    matrix = [i.split(' ') for i in TEST_TEXT.split('\n')]
    return matrix

def rotate_matrix(matrix, angle):
    matrix = parse_matrix(matrix)
    for k in range(angle / 90):
        rotated = []
        for i in range(len(matrix)):
            rotated.append([j[i] for j in matrix][::-1])
        matrix = rotated
    return rotated

def challenge():
    matrix = rotate_matrix(TEST_TEXT, 180)
    for i in matrix:
        for j in i:
            print  j + ' ',
        print ''

# # uncomment to run challenge
# challenge()
