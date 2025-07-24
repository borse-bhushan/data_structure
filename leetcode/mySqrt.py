from math import floor
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        old = 1 / 2 * (x / 2 + x / (x / 2))

        while True:
            new = 1 / 2 * (old + x / old)

            if abs(new - old) < 1e-6:
                return floor(new)
            old = new

print(Solution().mySqrt(8))
