#Write a Python program to accept a filename from the user and print the extension of that
file = input('give the file name with extension: ')
t = file.split(".")
print(t[1])