## SECRET SANTA
##
## challenge #247 (easy)
## https://redd.it/3yiy2d
##
##
## sarthak7u@gmail.com
##

import random

class Santa(object):
    def __init__(self, name, family):
        self.name = name
        self.family = family

def secret_santas(data):
    santas = []

    family_id = 0
    for i in data.splitlines():
        for j in i.split(' '):
            santas.append(Santa(j, family_id))
        family_id += 1

    unboxers = santas[:]


    final = {}
    while len(santas) > 0:
        santa = santas.pop(random.randrange(0, len(santas)))
        index = 0


        if santa.family == unboxers[index].family:
            while index < len(unboxers) - 1:
                index += 1
                if santa.family != unboxers[index].family:
                    final[santa.name] = unboxers.pop(index).name
                    break
                else:
                    continue
        else:
            final[santa.name] = unboxers.pop(index).name



    return final

sample_data ='''Sean
Winnie
Brian Amy
Samir
Joe Bethany
Bruno Anna Matthew Lucas
Gabriel Martha Philip
Andre
Danielle
Leo Cinthia
Paula
Mary Jane
Anderson
Priscilla
Regis Julianna Arthur
Mark Marina
Alex Andrea'''

## sample run
print(secret_santas(sample_data))
