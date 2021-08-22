# The code is to implement lambda function in program
# lambda function have many args, but only one expression .
# Syntax of lambda is :- lambda args : expr

# Declaration of lambda
sample_func = lambda x: x * 2

# Passing args in lambda function
print(sample_func(4))

# ------------------------------------------

# Declaration of lambda with if-else ....
sample_func2 = lambda x, y: x if x < y else y

print(sample_func2(1, 2))

# -------------------------------------------

# Declaration of lambda with filter() function ....

list_1 = [1, 2, 3, 4, 5]
sample_func3 = list(filter(lambda x: x % 2 != 0, list_1))

print(sample_func3)

# --------------------------------------------

# Declaration of lambda with map() function ....

list_2 = ["A", "B", "C", "D"]
sample_func4 = list(map(lambda x: x * 2, list_2))

print(sample_func4)

# ---------------------------------------------

# Declaration of lambda with reduce() function ....
from functools import reduce

list_3 = [1, 2, 3, 4, 5]
sample_func5 = reduce((lambda x, y: x * y), list_3)

print(sample_func5)
