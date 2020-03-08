# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
import datetime
from datetime import timedelta

date2 = datetime.date(2014, 7, 11)
date1 = datetime.date(2014, 7, 2)
timedelta = date2 - date1
print (timedelta)
print(timedelta.days) #both print out the result in a different manner