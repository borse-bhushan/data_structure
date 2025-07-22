class Solution:
    def romanToInt(self, roman_str: str) -> int:

        roman_map = {
            "I": 1,
            "V": 5,  # Non repeatable | I sub from only
            "X": 10,  # I sub from only
            "L": 50,  # Non repeatable
            "C": 100,
            "D": 500,  # Non repeatable
            "M": 1000,
        }

        total = 0
        prev_value = 0

        for chr in reversed(roman_str):

            numb = roman_map[chr]
            if numb < prev_value:
                total -= numb
            else:
                total += numb

            prev_value = numb

        return total


if __name__ == "__main__":
    print("OP: ", Solution().romanToInt("VIX"))
