## String Permutator
##
## challenge #12 (easy)
## https://redd.it/pxs2x
##
##
## sarthak7u@gmail.com

def permutator(lis):
    original_lis = lis
    permutations = []
    if len(lis) == 2:
        return [lis, lis[::-1]]
    else:
        for i in original_lis:
            lis = original_lis[:]
            lis.remove(i)
            if permutator(lis) != None:
                permutations.extend([[i] + j for j in permutator(lis)])
    return permutations

def string_permutator(string):
    permutations = []
    for i in permutator(range(len(string))):
        permutation = ""
        for j in i:
            permutation += string[j] 
        permutations.append(permutation)
    return permutations


