# This code Defines how map() function works ..
# Map just passes the list of variables into the functions and test out all outputs .

# Sample function
def sample_func(numbers):

    return numbers * 2


# Sample Iteration
input_list = [1, 2, 3, 4, 5]

# Object creation of map function
object = map(sample_func, input_list)

# map() function returns an object , so if you want specific output ,
# Don't forget to list out object with list() or tuple() function ....
print(list(object))
