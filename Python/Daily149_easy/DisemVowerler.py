## DISEMVOWELER
##
## challenge #149 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/
##
##
## sarthak7u@gmail.com
##

def disemvoweler(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    no_vowels, only_vowels = "", ""
    for i in text.replace(" ", ""):
        if i in vowels:
            only_vowels += i
        else:
            no_vowels += i
    return no_vowels, only_vowels
