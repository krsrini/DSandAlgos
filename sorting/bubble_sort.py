# Author           		: krsgit@yahoo.com 
# Creation Date    		: Tue Aug 23 11:20:20 PDT 2022

# Time complexity 
# average and worst cases : O(n²) 
# best case : O(n) 

# The bubble sort has a space complexity of O(1). 
# The number of swaps in bubble sort equals the number of inversion pairs in the given array. 
# When the array elements are few and the array is nearly sorted, bubble sort is effective and efficient

# stable sorting algorithm

def bubble_sort(arr):
    arrLen=len(arr)
    for i in range(arrLen):
        for j in range(arrLen-1, i, -1):
            if arr[j-1] > arr[j]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr

arr = [5, 8, 3, 9, 4, 1, 7]
result = bubble_sort(arr)
print(result)