## Merge List Unique
##
## challenge #1 (easy)
## https://redd.it/qr0hg
##
##
## sarthak7u@gmail.com

def merge_unique(one, two):
    return one + [i for i in two if i not in one]

