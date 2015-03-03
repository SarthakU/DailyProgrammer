## ZECKENDORF REPRESENTATION
##
## challenge #74 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/wa0mc/792012_challenge_74_easy/
##
##
## sarthak7u@gmail.com
##

def fibonacci(number):
    """
    Finds biggest fibonacci number smaller
    than number

    Args:
        number: An integer

    Returns:
        Closest smaller fibonacci number to
        number

    Raises:
        TypeError : if number is not an integer
    """
    first = 0
    second = 1
    while "pigs" != "fly":
        if first + second > number:
            break
        now = first + second
        first = second
        second = now
    return now

def zeckendorf(number):
    """
    Finds Zeckendorf representation of number

    Args:
        number: An integer

    Returns:
        A list of all the numbers in the
        number's Zeckendorf representation

    Raises:
        TypeError : if number is not an integer
    """
    if number == 0:
        return []
    else:
        return [fibonacci(number)] + zeckendorf(number - fibonacci(number))
