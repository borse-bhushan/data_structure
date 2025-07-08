"""
Problem Statement:
Given a sorted array nums, remove the duplicates in-place so that each unique element appears only once.
Return the count k of unique elements.
The first k elements of nums should hold the unique values in sorted order.

Input:

nums: list of integers sorted in non-decreasing order

Output:

Integer k: number of unique elements

Modified list nums with unique elements in first k positions

Example:

Input: nums = [1, 1, 2]
Output: 2
Modified nums: [1, 2, _]

Steps:
Use two pointers: i for the place to write, j to iterate.

Start i = 0. Loop j from 1 to end.

If nums[j] != nums[i], increment i, set nums[i] = nums[j].

Return i + 1 as the count of unique elements.
"""


def remove_duplicates_sorted(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    i += 1

    return nums[:i]

print(
    "OUT: ", remove_duplicates_sorted([1, 1, 1, 1, 2, 3, 3, 4, 5])
)
# OUT:  [1, 2, 3, 4, 5]
