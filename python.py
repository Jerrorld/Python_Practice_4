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
def rev_string(str):
    return str[::-1]

print(rev_string("tedious"))
print(rev_string("racecar"))



# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x,a,b):
  return x in range(a,b+1)
     
# returns a boolean
print(num_within(12,5,18))     
print(num_within(11,1,10))     

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#

# this is a pascal triangle using the power of 11
# note that it will only appropriately work up to 5 lines
def pascal(n): 
    # iterarte n
    for i in range(n):
        # adjust for space
        print(' '*(n-i), end='')
    
        # compute power of 11
        print(' '.join(map(str, str(11**i))))

pascal(5)
pascal(3)