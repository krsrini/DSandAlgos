
# Author           		: krsgit@yahoo.com 
# Creation Date    		: Mon Aug 15 18:50:19 PDT 2022
import random
def QuickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        QuickSort(arr, low, pivot-1)
        QuickSort(arr, pivot+1, high)

def partition(arr, low, high):

    pivot = arr[low]
    p = random.randint(low, high)
    arr[low],arr[p] = arr[p],arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i< high:
            i = i + 1
        while arr[j] > pivot:
            j = j - 1
        if (i < j):
            (arr[i],arr[j]) = (arr[j],arr[i])
    (arr[low],arr[j]) = (arr[j],arr[low])
    return j

#arr = [534, 246, 933, 127, 277, 321, 454, 565, 220]
#arr = [-913743, 3241, 999999, 1243153, 0, 0, 999999999]
#arr = [5, 3, 1, -10, -11, -100]
arr = [5, 8, 3, 9, 4, 1, 7]
QuickSort(arr, 0, len(arr)-1)
print(arr)