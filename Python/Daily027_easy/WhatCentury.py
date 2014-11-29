## WHAT CENTURY IS IT
##
## challenge #27 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/r0r3h/3172012_challenge_27_easy/
## 
## 
## sarthak7u@gmail.com
##
import Leapyear
def century(year):
	return (year/100) +1
year = int(raw_input("Enter Year : "))
print "Century    :", century(year)
print "Leap Year  :",
if Leapyear.isleapyear(year): print "Yes" 
else: print "No"