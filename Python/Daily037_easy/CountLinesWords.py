## COUNT LINES WORDS
##
## challenge #037 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/rzdwq/482012_challenge_37_easy/
##
##
## sarthak7u@gmail.com
##

def count_lines(filename):
    f = open(filename, "r")
    text = f.read()
    lines = 1
    for i in text:
        if i == "\n":
            lines += 1
    return lines

def count_words(filename):
    f = open(filename, "r")
    text = f.read()
    lines = text.split("\n")
    words = []
    for i in lines:
        temp = i.split(" ")
        for j in temp:
            if j != "" and j != "\t" and j != " ":
                words.append(j)
    return len(words)
