# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.
given_number = int(input("give a number: "))
existing_number = 17
print (existing_number-given_number)
if given_number > existing_number:
    print(2*abs(given_number-existing_number))
else:
    print("Given Number is less then 17")
