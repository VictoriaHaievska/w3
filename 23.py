# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.

def copies_string (str, n):
    if len(str) >= 2:
        return print(str[:2]*n)
    return print(str*n)

copies_string("La", 8)