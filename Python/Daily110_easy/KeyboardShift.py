## KEYBOARD SHIFT
##
## challenge #110 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/12k3xr/1132012_challenge_110_easy_keyboard_shift/
##
##
## sarthak7u@gmail.com
##

a = str(raw_input("Enter a string: ")).lower(); ans = ""
wrong = list("wertyuiop{[sdfghjkl;:xcvbnm,< ")
right = list("qwertyuioppasdfghjkllzxcvbnmm ")
for i in xrange(len(a)):
    ans += right[wrong.index(a[i])]
print ans
