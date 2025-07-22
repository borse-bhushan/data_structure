class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        if not s:
            return True

        open_parm = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        close_parm = {cl: op for op, cl in open_parm.items()}

        stck = []

        index = -1
        lnt = len(s) - 1

        while index != lnt:
            index += 1

            cur_ch = s[index]

            if cur_ch in open_parm:
                stck.append(cur_ch)

            else:
                if not stck:
                    return False
                while stck:
                    lst_val = stck[-1]

                    if close_parm[cur_ch] == lst_val:
                        stck.pop()
                        break
                    else:
                        return False
        if not stck:
            return True
        return False


print(Solution().isValid(")(){}"))
