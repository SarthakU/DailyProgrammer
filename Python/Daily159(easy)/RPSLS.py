## ROCK PAPER SCISSORS LIZARD SPOCK
##
## challenge #159 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/23lfrf/4212014_challenge_159_easy_rock_paper_scissors/
##
## sarthak7u@gmail.com

import random

print "WELCOME TO Rock paper scissors lizard spock!"
rules = str(raw_input("Do you want to view the rules(y/n)"))
if rules == "y":
    print """
    -Scissors cut Paper
    -Paper covers Rock
    -Rock crushes Lizard
    -Lizard poisons Spock
    -Spock smashes Scissors
    -Scissors decapitate Lizard
    -Lizard eats Paper
    -Paper disproves Spock
    -Spock vaporizes Rock
    -Rock crushes Scissors"""

    raw_input("Press enter to start playing")
print """
The codes:
    Rock     = 0
    Paper    = 1
    Scissors = 2
    Lizard   = 3
    Spock    = 4"""

userInput = int(raw_input("Enter your code here: "))
aiInput = random.randint(0,4)

legend = {0:"Rock", 1:"Paper", 2:"Scissors", 3:"Lizard", 4:"Spock"}


    
# contains all cases
thematrix = {(0,1):-1, (0,2):1, (0,3):1, (0,4):-1,
             (1,2):-1, (1,3):-1, (1,4):1,
             (2,3):1, (2,4):-1,
             (3,4):1}
print "Your said: ", legend[userInput]
print "Ai said: ", legend[aiInput]
if aiInput == userInput:
    print "Draw 'tis"
elif aiInput > userInput:
    result = thematrix[(userInput,aiInput)]
    if result ==1:
        print "You win"
    elif result == -1:
        print "The computer wins"
elif aiInput < userInput:
    result = thematrix[(aiInput,userInput)]
    if result == -1:
        print "You win"
    elif result == 1:
        print "The computer wins"
