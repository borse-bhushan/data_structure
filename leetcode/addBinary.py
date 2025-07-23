class Solution:
    def addBinary(self, a: str, b: str) -> str:

        len_a = len(a)
        len_b = len(b)

        if len_a != len_b:
            if len_a > len_b:
                b = "0" * (len_a - len_b) + b
            else:
                a = "0" * (len_b - len_a) + a

        index = len(a) - 1

        carry = 0
        output_str = ""

        map_obj = {0: ["0", 0], 1: ["1", 0], 2: ["0", 1]}

        while index != -1:
            add = int(a[index]) + int(b[index]) + carry

            at_str, carry = map_obj.get(add, ["1", 1])
            output_str += at_str

            index -= 1

        if carry:
            output_str += "1"

        return output_str[::-1]


print(Solution().addBinary(a="1111", b="1111"))
