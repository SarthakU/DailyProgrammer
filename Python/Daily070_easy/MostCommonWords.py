## MOST COMMON WORDS
##
## challenge #70 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/vsv3g/6292012_challenge_70_easy/
##
##
## sarthak7u@gmail.com
##

def most_common_words(filename, n):
    """
    Finds n most common words in text file filename.

    Args:
        filename: name of text file
        n : number of words to find

    Returns:
        A list of tuples, containing word and number of its occurences
        in that order. Fo example
        [('the', 32), ('of', 20), ('and', 19), ('is',16)]

    Raises:
        IOError: File does not exist.

    """
    # read the file
    text = open(filename, "r").read()

    # get all words from file
    lines = text.split("\n")
    words = {}
    for i in lines:
        temp = i.split(" ")
        for j in temp:
            if j != "" and j != "\t" and j != " ":
                if j not in words:
                    words[j] = 1
                else:
                    words[j] += 1

    # sort words according to number of occurences
    most_common = [(i,words[i]) for i in sorted(words, key=words.get, reverse=True)]

    # get n most common words
    most_common_n = []
    for i in xrange(0,n):
        most_common_n.append(most_common[i])

    return most_common_n
