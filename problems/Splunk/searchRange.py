'''
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''
def searchRange(nums, target):
    def search_first(nums, target):
        size = len(nums)
        begin_position = -1
        start = 0
        end = size - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                begin_position = mid
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return begin_position

    def search_end(nums, target):
        size = len(nums)
        start = 0
        end = size - 1
        end_position = -1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                end_position = mid
                start = mid + 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return end_position

    return [search_first(nums, target), search_end(nums, target)]

#nums = [5,7,7,8,8,10]
#target = 8
#nums = [1,2,3]
#target = 1
nums = [2,2]
target = 2
print(searchRange(nums, target))