"""
Problem Statement:
Given an integer array nums, find the contiguous subarray (of at least one element) with the maximum sum, and return that sum.

Input:

nums: list of integers (can include negatives)

Output:

Integer: maximum subarray sum

Example:

python
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
# Subarray: [4, -1, 2, 1]
Steps:

Set both current_sum and max_sum to first element.
Loop from the second element to end:
Update current_sum = max(current number, current_sum + current number)
Update max_sum = max(max_sum, current_sum)
Return max_sum.

"""


def maximum_subarray(nums):

    max_sum = nums[0]
    current_sum = nums[0]

    for ele in nums[1:]:
        current_sum = max(ele, current_sum + ele)
        max_sum = max(max_sum, current_sum)

    return max_sum


print("OUT: ", maximum_subarray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
