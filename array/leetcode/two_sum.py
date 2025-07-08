"""
Problem Statement:
You are given an array of integers nums and an integer target.
Your task is to find two distinct indices i and j in the array such
that nums[i] + nums[j] == target. Return the indices [i, j].
You may assume that exactly one solution exists,
and you may not use the same element twice.

Input:
A list of integers: nums (length between 2 and 10⁴)
An integer: target

Output:
A list containing two integers: the indices of the elements that add up to target

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]  # because nums[0] + nums[1] = 2 + 7 = 9

"""

def two_sum(nums, target):
    "Brute force"

    results = []
    for index in range(0, len(nums)-1):
        current_num = nums[index]

        for next_index in range(index+ 1, len(nums)):
            if (nums[next_index] + current_num) == target:
                results.append([index, next_index])

    return results


print(
    two_sum(nums=[2, 7, 11, 15, 8, 1], target=9)
)


def with_dict(nums, target):
    """
    Optimized version.
    """

    visited_numbers = {}

    results = []

    for index, num in enumerate(nums):

        required_value = target - nums

        if required_value in visited_numbers:
            results.append([visited_numbers[num], index])

        visited_numbers[num] = index


print(
    two_sum(nums=[2, 7, 11, 15, 8, 1], target=9)
)
