# Author           		: krsgit@yahoo.com 
# Creation Date    		: Tue Aug 23 18:34:11 PDT 2022

# Time complexity : O(n*Log n) 

# The merge sort has a space complexity of O(n).

# stable sorting algorithm 


def merge_sort(arr):
    if len(arr) > 1:
        left_array = arr[ : len(arr)//2 ]
        right_array = arr[ len(arr)//2 : ]

        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1
        
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1
        
        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1

    return arr


arr = [5, 8, 3, 9, 4, 1, 7]
result = merge_sort(arr)
print(result)