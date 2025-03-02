def dutch_flag_sort(arr):
    first = "R"
    second = "G"
    third = "B"
    left = 0
    right = len(arr) - 1
    i = 0
    while i <= right:
        if arr[i] == first:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        elif arr[i] == right:
            arr[i], arr[right] = arr[right], arr[i]
            i += 1
            right -= 1
        else:
            i += 1
    
    return arr

arr = ["G", "B", "G", "G", "R", "B", "R", "G"]
print(dutch_flag_sort(arr)) 