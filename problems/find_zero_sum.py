def find_zero_sum(arr):
    arr.sort()
    size = len(arr)
    result = set()
    for i in range(size):
        current_element = arr[i]
        left = i + 1
        right = size - 1
        while left < right:
            sum = current_element + arr[left] + arr[right]
            if sum == 0:
                result.add(f"{arr[i]},{arr[left]},{arr[right]}")
                left += 1
            elif sum > 0:
                right -= 1
            else:
                left += 1
    return list(result) 

#arr = [10, 3, -4, 1, -6, 9]
arr = [0, 0, 0,0]
#expected Output : ["10,-4,-6", "3,-4,1"]

print(find_zero_sum(arr))