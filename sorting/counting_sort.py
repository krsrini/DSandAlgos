#!/usr/bin/env python

def counting_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    n = len(arr)
    min_arr = min(arr)
    max_arr = max(arr)
    freq = {}

    for i in range(0,n):
        if arr[i] not in freq:
            freq[arr[i]] = 1
        else:
            freq[arr[i]] += 1

    #print(freq)

    arr_index = 0
    for i in range(min_arr, max_arr+1):
        if i in freq:
            conc_seq = freq[i]
            #print(conc_seq,freq[i])
            while conc_seq > 0:
                arr[arr_index] = i 
                conc_seq -= 1
                arr_index += 1 
    return arr

#arr = [1, 4, 1, 2, 7, 5, 2]
arr = [5, 8, 3, 9, 4, 1, 7]
print(counting_sort(arr))