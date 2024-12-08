def my_function(a, b):
    if a > b:
        return a
    return b

result = my_function(5, 2)
print(result)  # Output: 5

result = my_function(2, 5)
print(result)  # Output: 5

#Bug: The function is not correctly comparing the values.
#In the case where a is less than b, it should return b. However, it returns a, leading to incorrect results when a < b