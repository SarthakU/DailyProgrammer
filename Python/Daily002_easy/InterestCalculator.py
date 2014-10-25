## INTEREST CALCULATOR
##
## challenge #2 (easy)
## http://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
##
## sarthak7u@gmail.com

#computes simple interest
def simpleInterest(principle, rate, timePeriod):
	return principle * (rate/100) * timePeriod

#computes compound interest
def compoundInterest(principle, rate, timePeriod):
	return (principle * ((1 + (rate/100))**timePeriod)) - principle

principle = float(raw_input("Enter the Principle amount: "))
rate = float(raw_input("Enter the interest rate: "))
timePeriod = float(raw_input("Enter the time period: "))
choice = float(raw_input("Enter 0 for simple, 1 for compounded interest\n"))

if choice == 0:
	print "The simple interest is: ", simpleInterest(principle, rate, timePeriod)
elif choice == 1:
	print "The compound interest is: ", simpleInterest(principle, rate, timePeriod)