# Code is to Explain how Bubble sort works

# Function for Bubble-Sort
def bubbleSort(arr):
    # Defining length of array
    length = len(arr)
    # For loop for first variable
    for first_num in range(length-1):
        # For loop for second variable
        for second_num in range(length-first_num-1):
            # If second number means current element is greater than its after-element
            if arr[second_num] > arr[second_num+1]:
                # Swap those elements with these formula
                arr[second_num], arr[second_num+1] = arr[second_num+1], arr[second_num]


# Creating a list
bubble_list = [7, 72, 90, 21, 60]

# Function Calling
bubbleSort(bubble_list)

print(bubble_list)

