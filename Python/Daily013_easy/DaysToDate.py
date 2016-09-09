## Days To Date
##
## challenge #13 (easy)
## https://redd.it/pzo4w
##
##
## sarthak7u@gmail.com

def days_to_date(day, month, leap=False):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap: 
        days[1] = 29
    return sum(days[:month - 1]) + day 
