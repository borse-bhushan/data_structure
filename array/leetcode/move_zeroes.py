"""
Problem Statement:
Given an array nums, move all 0s to the end while preserving the order of the non-zero elements.
This must be done in-place, using minimal operations.

Input:

nums: list of integers

Output:

Nothing returned

nums should be modified in-place so non-zero elements come first, followed by zeros

Example:

Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Steps:

Initialize pointer non_zero_index = 0.

Loop through array:

If value ≠ 0, move it to non_zero_index and increment.

After all non-zero elements are in place, fill the rest with 0s.
"""


def move_zeroes(nums):

    non_zero_index = 0

    for index in range(0, len(nums)):

        if nums[index] != 0:
            nums[non_zero_index] = nums[index]
            non_zero_index += 1

    for index in range(non_zero_index, len(nums)):
        nums[index] = 0
    return nums


print("OUT: ", move_zeroes(nums=[0, 1, 0, 3, 12, 0]))
