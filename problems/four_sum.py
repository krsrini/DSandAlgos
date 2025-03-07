# Given a list of numbers, find all the unique quadruples that sum up to a given target value.
'''
Example : 
Input

{
"arr": [0, 0, 1, 3, 2, -1],
"target": 3
}

Expected Output:

[
[-1, 0, 1, 3],
[0, 0, 1, 2]
]
'''
def four_sum(arr, target):
    result = []
    quad = []
    arr.sort()
    size = len(arr)

    if size < 4:
        return result

    def ksum(k, start, target):
        if k != 2:
            for i in range(start, size - k + 1):
                if i > start and arr[i] == arr[i - 1]:
                    continue
                quad.append(arr[i])
                ksum(k - 1, i + 1, target - arr[i])
                quad.pop()
        else:
        #calculate two sum
            left = start
            right =  size - 1
            while left < right:
                if (arr[left] + arr[right]) < target:
                    left += 1
                elif (arr[left] + arr[right]) > target:
                    right -= 1
                else:
                    result.append(quad + [arr[left] , arr[right]])
                    left += 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1


    ksum(4, 0, target)
    return result

arr = [0, 0, 1, 3, 2, -1]
target = 3

print(four_sum(arr, target))