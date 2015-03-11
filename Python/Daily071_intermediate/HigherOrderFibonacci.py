## HIGHER ORDER FIBONACCI
##
## challenge #71 (intermediate)
## http://www.reddit.com/r/dailyprogrammer/comments/vx3db/722012_challenge_71_intermediate/
##
##
## sarthak7u@gmail.com
##

def higher_k_fibonacci(k, N):
    '''
    Finds the N the term of Fibonacci series
    order k

    Args:
        k: order of desired Fibonacci series
        N: index of term in series need

    Returns:
        An int. the N th term in Fibonacci
        series of order k
    '''

    # add zeroes according to k
    series = [0 for i in xrange(0,k-1)]

    # add the 1 after all zeroes
    series.append(1)

    # obtain other terms by summ previous k terms
    for i in xrange(0,N):
        series.append(sum(series[-1:-(k+1):-1]))

    return series[N]
