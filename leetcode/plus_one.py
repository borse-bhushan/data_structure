from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [i for i in str(int("".join([str(i) for i in digits])) + 1)]


print(Solution().plusOne([1, 2, 4]))
