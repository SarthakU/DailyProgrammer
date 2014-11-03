## AGE PLUS PLUS
##
## challenge #20 (intermediate)
## http://www.reddit.com/r/dailyprogrammer/comments/qnkpp/382012_challenge_20_intermediate/
## 
## 
## sarthak7u@gmail.com
##

def main():
	age = int(raw_input("How old are you? : "))	
	age_months = age * 12
	age_days = age * 365
	age_hours = age_days * 24
	age_minutes = age_hours * 60
	age_seconds = age_minutes * 60

	print "Your age in months : ", age_months
	print "Your age in days : ", age_days
	print "Your age in hours : ", age_hours
	print "Your age in minutes : ", age_minutes
	print "Your age in seconds : ", age_seconds

main()


