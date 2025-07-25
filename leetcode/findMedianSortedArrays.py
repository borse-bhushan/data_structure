from typing import List


class Solution:

    def merge_two_arrays(self, l1: List[int], l2: List[int]):

        result = []
        while l1 and l2:

            if l1[0] < l2[0]:
                result.append(l1.pop(0))
            else:
                result.append(l2.pop(0))
        result += l1
        result += l2
        return result, len(result)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result, lnt = self.merge_two_arrays(nums1, nums2)
        if lnt % 2:
            mid = int(lnt / 2)
            return result[mid]
        else:
            mid = int(lnt / 2)
            return (result[mid-1] + result[mid]) / 2


print("\n\n\nOP: ", Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
