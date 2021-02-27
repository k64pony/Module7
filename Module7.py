#Assignment 1
import sys
import datetime

data = datetime.datetime.now()
print("The current datetime is: ")
print(data)

#Assignment 2
import sys
import datetime
from datetime import timedelta
dt = datetime.datetime.now()
addyears = datetime.timedelta(days=730)
minussecs = datetime.timedelta(seconds = 60)
date = dt+addyears-minussecs
print("The timedelta of current date plus two years minus 60 seconds is: ")
print(date)

#Assignment 3
import sys
import datetime
from datetime import timedelta
d = timedelta(days = 100, hours = 10, minutes = 13)
(d.days, d.seconds, d.microseconds)
(-1, 86399, 999999)
print("The timedelta object for 100 days, 10 hours and 13 minutes is: ")
print(d)

#Assignment 4
import sys
import datetime
from datetime import date

def currentage(birthDate): 
 today = datetime.datetime.now()
 age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
  
 return age  

print("My current age is: ")
print(currentage(date(1977, 12, 20)), "years old") 
