# Write a Python function called max_num()to find the maximum of three numbers.
def max_list(a, b, c):
    return max([a, b, c])

print(max_list(17, 38, 11))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(lst):
    if len(lst) is 0:
        return 0

    prod = lst[0]

    if len(lst) >1:
        for i in lst[1:]:
            prod = prod * i
    return prod

print(mult_list([]))
print(mult_list([3,5,2]))

# Write a Python function called rev_string() to reverse a string.
# Write a Python function called num_within() to check whether a number falls in a given range.
# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#