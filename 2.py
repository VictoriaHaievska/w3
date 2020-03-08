#Write a Python program to get the Python version you are using
import sys
print(sys.version)

#Write a Python program to display the current date and time.
# Sample Output :
# # Current date and time :
# # 2014-07-05 14:34:14
import datetime
print(datetime.datetime.now())

# Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
from math import pi

R = float(input("Radius: "))
S = pi * R**2
print (S)

#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
Name = input("Name?: ")
Surname = input ("Surname? ")
print("Hello, " + Surname + " " + Name)