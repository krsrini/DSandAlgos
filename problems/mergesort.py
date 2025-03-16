def mergesort(arr):
    if len(arr) > 1:
        left = arr[ : len(arr)//2]
        right = arr[len(arr)//2: ]

        print(left, right)
        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1  
            k += 1          

        while j < len(right):
            arr[k] = right[j]
            j += 1  
            k += 1

        return arr
def sortArray(nums):

    return mergesort(nums)

nums = [5,2,3,1]
print(sortArray(nums))