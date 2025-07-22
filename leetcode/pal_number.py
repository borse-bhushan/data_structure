class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        _x = x
        number = 0
        while x > 0:
            temp = x % 10
            x = x // 10

            number = number * 10 + temp

        return number == _x


if __name__ == "__main__":
    print(
        "isPalindrome >> ", Solution().isPalindrome(-121)
    )


# 3, 2, 1

# 3 * 10
# + 2
# == 32

# 32 * 10
# 320 + 1
