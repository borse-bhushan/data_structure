from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def convertLLtoL(self, ll1: ListNode, ll2: ListNode):

        while ll1:
            self.s1.append(ll1.val)
            ll1 = ll1.next

        while ll2:
            self.s2.append(ll2.val)
            ll2 = ll2.next

    def add_zeros(self, li: list, how_many, b=True):

        for i in range(how_many):
            # if b:
            li.append(0)
            # else:
            #     li.insert(0, 0)
        return

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        self.convertLLtoL(l1, l2)

        ls1 = len(self.s1)
        ls2 = len(self.s2)

        if ls1 > ls2:
            self.add_zeros(self.s2, ls1 - ls2, b=True)
        elif ls1 < ls2:
            self.add_zeros(self.s1, ls2 - ls1, b=True)

        c = 0
        result = []
        for i, z in zip(self.s1, self.s2):
            o = i + z + c
            if o > 9:
                c = o // 10
                result.append(o % 10)
            else:
                result.append(o)
                c = 0

        if c:
            result.append(c)
        return self.build_linked_list(result)

    def build_linked_list(self, values):
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head


s = Solution()
l1 = s.build_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = s.build_linked_list([9, 9, 9, 9])

head = s.addTwoNumbers(l1, l2)
st = []
while head:
    st.append(head.val)

    head = head.next


print("FINAL: ", st)
