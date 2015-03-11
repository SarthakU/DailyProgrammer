## NONOGRAM PUZZLE
##
## challenge #59 (intermediate)
## http://www.reddit.com/r/dailyprogrammer/comments/uh03h/622012_challenge_59_intermediate/
##
##
## sarthak7u@gmail.com

inputMatrix = [[0, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0]]
bottomClues = [u'']
topClues = [u'']

# gets clues for horizontal
for i in inputMatrix:
    index = 0
    while True:
        if i[index] == 0:
            if index != 0:
                bottomClues.append(u'')
        elif i[index] == 1:
            if type(bottomClues[-1]) != int:
                bottomClues.append(1)
            else:
                bottomClues[-1] +=1
        if index == len(i) - 1:
            bottomClues.append("\n")
            break
        index += 1

# gets clues for vertical
for i in range(0, len(inputMatrix[0])):
    index = 0
    while True:
        if inputMatrix[index][i] == 0:
            if index != 0:
                topClues.append(u'')
        elif inputMatrix[index][i] == 1:
            if type(topClues[-1]) != int:
                topClues.append(1)
            else:
                topClues[-1] += 1
        index += 1
        if index == len(inputMatrix[0]) - 1:
            topClues.append("\n")
            break

# prints topClues
for i in topClues:
    if type(i) != unicode:
        print i,

print ""

# prints bottomClues
for i in bottomClues:
    if type(i) != unicode:
        print i,
