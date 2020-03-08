# Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


def check (sp_value, list_values):
    for value in list_values:
        if sp_value == value:
            return True
        return False

test_list = [1,5,7,9,4,6,1,44,6,3]
print (check(10, test_list))