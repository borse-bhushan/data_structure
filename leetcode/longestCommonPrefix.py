from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        longest_prefix = ""

        for i in range(len(strs) - 1):

            for j in range(i + 1, len(strs)):
                temp = ""

                for ch1, ch2 in zip(strs[i], strs[j]):
                    if ch1 == ch2:
                        temp += ch1
                    else:
                        break

                if longest_prefix:
                    if len(longest_prefix) < len(temp):
                        break

                if temp != longest_prefix:
                    longest_prefix = temp

            if not longest_prefix:
                break

        return longest_prefix


print(Solution().longestCommonPrefix(["acc", "aaa", "aaba"]))
