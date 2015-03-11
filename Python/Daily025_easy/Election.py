## ELECTION
##
## challenge #25 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/qxuug/3152012_challenge_25_easy/
##
##
## sarthak7u@gmail.com
##

def election(args,totalvotes):
    """Takes list containing lists
    of two elements name and votes
    returns name of element which is
    in majority otherwise says not in majority"""
    index = 0
    for i in args:
        if args[index][1] > totalvotes/2:
            return args[index]
        index+=1
    else:
        return ["No candidate in majority"]

def main():
    candidates = []
    number_of_candidates = int(raw_input("Number of candidates: "))
    total_votes = 0
    print "~~~~~~~~~~~~~~~~~~~~~~"
    print ""
    for i in xrange(0, number_of_candidates):
        name = raw_input("Name of candidate: ")
        votes = int(raw_input("Votes for candidate: "))
        candidates.append([name,votes])
        total_votes += votes
        print ""
        print "~~~~~~~~~~~~~~~~~~~~~~"
        print ""
    print election(candidates, total_votes)[0]
main()
