# Author           		: krsgit@yahoo.com 
# Creation Date    		: Tue Aug 30 12:22:04 PDT 2022
# Time Complexity Of Selection Sort : O(n log n)
# The space complexity of Selection Sort is O(1). 
# Not a stable sorting algorithm

def heapify(arr,arrLen,i):
    largest = i
    left = (i * 2) + 1
    right = (i * 2) + 2
    
    if left < arrLen and arr[i] < arr[left]:
        largest = left
    
    if right < arrLen and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        #Swap
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, arrLen, largest)

def heap_sort(arr):
    arrLen = len(arr)
    #Build Max Heap
    for i in range(arrLen//2, -1, -1):
        heapify(arr,arrLen,i)
    
    # element extraction
    for i in range(arrLen-1, 0, -1):
        # Swap
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
    return arr

arr = [5, 8, 3, 9, 4, 1, 7]
result = heap_sort(arr)
print(result)
