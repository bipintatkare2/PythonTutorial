# The code is to implement filter() method
# filter(func, iter) method is used to filter/select same element in func & iter
# It returns same element in function and iteration

file_open = open("Advance Functions/filter_sample.txt", "r")
content = file_open.readlines()
friends_list = []

for name in content:
    if name != content[len(content) - 1]:
        actual_name = name[:-1]
        friends_list.append(actual_name)
    else:
        friends_list.append(name)


def best_friends(params):
    friends = ["Bipin", "Shubham", "Aditya", "Shailesh"]

    if params in friends:
        return True
    else:
        return False


filtered_list = filter(best_friends, friends_list)

closed_list = tuple(filtered_list)

print(closed_list)
