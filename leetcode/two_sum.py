from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for main_ind in range(len(nums) - 1):
            found = False
            for sub_ind in range(main_ind + 1, len(nums)):
                if nums[main_ind] + nums[sub_ind] == target:
                    found = True
                    result.extend([main_ind, sub_ind])
                    break
            if found:
                break
        return result


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], target=9))
