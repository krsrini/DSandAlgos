
# Author           	        : krsgit@yahoo.com 
# Creation Date    	        : Mon Aug 15 18:50:19 PDT 2022
# Average Time complexity   : O(N log(N))
# WORST TIME COMPLEXITY	    : O(n²) 
# Space Complexity          : O(N)

import random
def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)
    return arr

def quick_sort_helper(arr, low, high):
    if low < high:
        pivot = partition(arr,low,high)
        quick_sort_helper(arr,low,pivot-1)
        quick_sort_helper(arr,pivot+1,high)
    else:
        return arr
        
def partition(arr, low, high):
    i = low
    j = high

    p = random.randint(low, high)
    arr[low],arr[p]=arr[p],arr[low]
    pivot = arr[low]

    while i < j :
        while arr[i] <= pivot and i < j:
            i += 1 
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[low],arr[j]=arr[j],arr[low]
    return j


#arr = [534, 246, 933, 127, 277, 321, 454, 565, 220]
#arr = [-913743, 3241, 999999, 1243153, 0, 0, 999999999]
#arr = [5, 3, 1, -10, -11, -100]
arr = [5, 8, 3, 9, 4, 1, 7]
result = quick_sort(arr)
print(result)