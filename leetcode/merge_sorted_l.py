from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        result = []

        nums = nums1[:m]

        while nums and nums2:

            if nums[0] < nums2[0]:
                result.append(nums.pop(0))
            else:
                result.append(nums2.pop(0))

        result += nums
        result += nums2

        nums1.clear()
        for ind, val in enumerate(result):
            nums1.append(val)


nums1 = [1, 2, 3, 0, 0, 0]
Solution().merge(nums1=nums1, m=3, nums2=[2, 5, 6], n=3)
print(nums1)
