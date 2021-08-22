# The code is to implement reduce() function ..
# It summarize all inputs and gives only one output
# According to their function working
# Requirement is you have to import 'functools' module
# reduce() is used to apply to a particular function only

import functools


def func(x, y):
    return x * y


list_1 = [1, 2, 3, 4, 5]

# This var will return only single output
funct = functools.reduce(func, list_1)

print(funct)
