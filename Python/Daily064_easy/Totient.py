## TOTIENT
##
## challenge #64 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/uzx8b/6132012_challenge_64_easy/
##
##
## sarthak7u@gmail.com
##

import fractions
def divisors(num):
    """
    Finds all the divisors of num

    Args:
        num: A number to find divisors of

    Returns:
        A list of all the divisors of num

    Raises:
        TypeError : if num is not an integer
    """
    divisors = []
    for i in xrange(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def number_of_divisors(num):
    """
    Finds number of divisors of num

    Args:
        num: A number to find divisors of

    Returns:
        An int, the number of divisors of num

    Raises:
        TypeError : if num is not an integer
    """
    return len(divisors(num))

def sum_of_divisors(num):
    """
    Finds sum of al divisors of num

    Args:
        num: A number to find divisors of

    Returns:
        An int, the sum of divisors of num

    Raises:
        TypeError : if num is not an integer
    """
    return sum(divisors(num))

def totatives(num):
    """
    Finds all the totatives of num

    Args:
        num: A number to find totatives of

    Returns:
        A list of all the totatives of num

    Raises:
        TypeError : if num is not an integer
    """
    totatives = []
    for i in xrange(1,num+1):
        if fractions.gcd(i,num) == 1:
            totatives.append(i)
    return totatives

def number_of_totatives(num):
    """
    Finds number of totatives of num

    Args:
        num: A number to find totatives of

    Returns:
        A int, number of totatives of num

    Raises:
        TypeError : if num is not an integer
    """
    return len(totatives(num))
