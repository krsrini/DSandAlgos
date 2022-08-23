# Author           		: krsgit@yahoo.com 
# Creation Date    		: Tue Aug 23 11:20:20 PDT 2022

# Time Complexity Of Selection Sort
# Best Case — O(n²)
# Average Case — O(n²)
# Worst CaseO — O(n²)

# The space complexity of Selection Sort is O(1). This is because we use only constant extra space such as: 2 variables to enable swapping of elements. One variable to keep track of smallest element in unsorted array

# Not a stable sorting algorithm

def selection_sort(arr):
    arrLen=len(arr)
    for i in range(arrLen):
        minValIndex = i
        for j in range(i+1, arrLen):
            if arr[j]<arr[minValIndex]:
                minValIndex=j
        (arr[i],arr[minValIndex])=(arr[minValIndex],arr[i])
    return(arr)

arr = [5, 8, 3, 9, 4, 1, 7]
result = selection_sort(arr)
print(result)

