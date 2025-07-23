class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return -1
        if not haystack:
            return -1

        st_ind = 0

        lnt = len(haystack)
        slide = len(needle) - 1

        if (slide + 1) > lnt:
            return -1

        while slide != lnt:

            if haystack[st_ind : slide + 1] == needle:
                return st_ind

            slide += 1
            st_ind += 1

        return -1


haystack = "abb"
needle = "abaaa"

Solution().strStr(haystack=haystack, needle=needle)
