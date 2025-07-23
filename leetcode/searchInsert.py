from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:

        for index, num in enumerate(nums):
            if num == target:
                return index

            elif num > target:
                return index - 1

        return index + 1


Solution().searchInsert(nums=[1, 3, 5, 6], target=5)
