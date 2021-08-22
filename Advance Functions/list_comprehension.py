# Code explains how list comprehension with different function works ..

# Syntax for list comprehension is ...
# newList = [ expression(element) for element in oldList if condition ]
# Note that element and iterator(element in for loop) should be same as they called to each other while procedure ...

# Simple demonstration of list comp.

List = [letters for letters in "BipinTatkare"]

# Another eg. of list comp. is ,

newList = [i * 2 for i in range(10)]

# Nested List Comp. is similar to nested for loops ...
# Here is the example .

# Here, we declare a list with another list inside the root and
# it generates 0 to 4 numbers in a list format ..

nested_list = [[num for num in range(5)] for numb in range(5)]
# Output :- [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

# if we want to extract upper list which is of each number is in one list ,
# here is the solution ..

flattern_list = [value for sub in nested_list for value in sub if value < 3]
# Output :- [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

# -----------------------------------------------------------------------------

