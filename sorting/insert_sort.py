# Author           		: krsgit@yahoo.com 
# Creation Date    		: Tue Aug 23 17:06:23 PDT 2022
# Time complexity 
# average and worst cases : O(n²) 
# best case : O(n) 
# The insertion sort has a space complexity of O(1).
# stable sorting algorithm 

def insert_sort(arr):
    arrLen = len(arr)
    for i in range(1,arrLen):
        j = i
        while j > 0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -=1
    return arr

arr = [5, 8, 3, 9, 4, 1, 7]
result = insert_sort(arr)
print(result)