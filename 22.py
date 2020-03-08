#Write a Python program to count the number 4 in a given list.

def quantity_four (numbers):
    num = 0
    for number in numbers:
        if number ==4:
            num = num+1
    return print(num)

quantity_four(range(10))