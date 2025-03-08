# Leetcode # 259
# 3 Sum Smaller

def count_triplets(target, numbers):
    result = 0
    numbers.sort()
    size = len(numbers)
    for i in range(size):
        left = i + 1
        right = size -1
        while left < right:
            three_sum = numbers[i] + numbers[left] + numbers[right]
            if three_sum < target:
                result += right - left
                left += 1
            else:
                right -= 1
    return result

# target =  4
# numbers =  [5, 0, -1, 3, 2]
# expected output : 2

target =  4
numbers =  [3,1,0,-2]
# expected output : 3

print(count_triplets(target, numbers))