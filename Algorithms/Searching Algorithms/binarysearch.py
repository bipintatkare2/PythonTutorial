# Code is to explain how binary search works


def binarySearch(arr, start, end, number):

    if end >= start:
        mid = start+(end-1)//2
        if arr[mid] == number:
            return mid
        elif arr[mid] > number:
            return binarySearch(arr, start, mid-1, number)
        else:
            return binarySearch(arr, mid+1, end, number)
    else:
        return -1


binary_list = [10, 20, 30, 40, 50]
length_list = len(binary_list)
search_num = 40

result = binarySearch(binary_list, 0, length_list-1, search_num)

if result != -1:
    print("Element present at index: {}".format(result))
else:
    print("Element is not present")
