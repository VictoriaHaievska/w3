# Write a Python program to find whether a given number (accept from the user) is even or odd,
# print out an appropriate message to the user.

def evaluation_number (n):
    if n%2 == 0:
        return print("THis is an even number")
    return print ("This is an odd number")

n = int(input("Number: "))
evaluation_number(n)