# time complexity: O(n)
# space complexity: O(1)

def segregate_evens_and_odds(arr):
    pass
    size = len(arr)
    left = 0
    right = size - 1
    while left < right:
        if (arr[left] % 2) == 0:
            left += 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
    
    return arr    
arr = [5, 8, 3, 9, 4, 1, 7]
print(segregate_evens_and_odds(arr))  # Output: [8, 4, 5, 9, 3, 1, 7]