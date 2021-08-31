# Code is to explain how insertion sort works


def insertionSort(arr):

    for first in range(1, len(arr)):

        key = arr[first]
        j = first-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


insertion_list = [20, 10, 30, 50, 40, 80, 60, 70]

insertionSort(insertion_list)

