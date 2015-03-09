## QUICKSORT
##
## challenge #177 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/2ejl4x/8252014_challenge_177_easy_quicksort/
##
##
## sarthak7u@gmail.com
##

def quick_sort(unsorted):
    # if list empty return
    # else set first element as pivot
    if len(unsorted) == 0:
        return []
    else:
        pivot = unsorted[0]

    # divide in two - larger and smaller than pivot
    smaller, larger = [], []
    for i in unsorted:
        if i > pivot:
            larger.append(i)
        elif i < pivot:
            smaller.append(i)

    return quick_sort(smaller) + [pivot] + quick_sort(larger)
