# Code is to show how linear search works


def linear_search(linear_list, length_list, search_num):

    for num in range(0, length_list):
        if linear_list[num] == search_num:
            return num

    return -1


linear_list = [10, 20, 30, 40]
search_num = 10
length_list = len(linear_list)

result = linear_search(linear_list, length_list, search_num)

if result == -1:
    print("Element is not present")
else:
    print("Element is present at index {}".format(result))

