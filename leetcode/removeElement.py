from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            if val == nums[0]:
                return 0
            return 1

        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


val = 2
nums = [1, 2, 3]


op = Solution().removeElement(nums, val)
print("OP: ", op)
print("nums: ", nums[:op])
