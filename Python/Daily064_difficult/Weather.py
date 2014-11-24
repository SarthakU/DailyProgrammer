## WEATHER
##
## challenge #64 (difficult)
## http://www.reddit.com/r/dailyprogrammer/comments/uzx7y/6132012_challenge_64_difficult/
## 
## 
## sarthak7u@gmail.com
import requests 

city = raw_input("Enter you city: ")
data = requests.get("http://api.openweathermap.org/data/2.5/find?units=metric&q=%s" % city)
weather = data.json()['list'][0]['main']
print """
	Weather for %s
_________________________________
""" % city

print ' Temprature  : %u C ' % weather['temp']
print " Humidity    : %s   " % weather['humidity']
print " Pressure    : %s Pa" % weather['pressure']
print " MaxTemp     : %s C " % weather['temp_max']
print " MinTemp     : %s C " % weather['temp_min']